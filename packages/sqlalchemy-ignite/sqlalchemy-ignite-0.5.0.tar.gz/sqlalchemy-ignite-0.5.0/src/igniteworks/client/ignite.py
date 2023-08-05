# -*- coding: utf-8; -*-
#
# Copyright (c) 2020 - 2021 Dr. Krusche & Partner PartG. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
# @author Stefan Krusche, Dr. Krusche & Partner PartG
#

import logging
import re

from pyignite import Client

from igniteworks.client.exceptions import ProgrammingError

logger = logging.getLogger(__name__)

"""
'query_fields': [
    {'name': 'ID', 'type_name': 'java.lang.Integer', 'is_key_field': True, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': -1, 'scale': -1},
    {'name': 'NAME', 'type_name': 'java.lang.String', 'is_key_field': False, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': 35, 'scale': -1},
    {'name': 'COUNTRYCODE', 'type_name': 'java.lang.String', 'is_key_field': True, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': 3, 'scale': -1},
    {'name': 'DISTRICT', 'type_name': 'java.lang.String', 'is_key_field': False, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': 20, 'scale': -1},
    {'name': 'POPULATION', 'type_name': 'java.lang.Integer', 'is_key_field': False, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': -1, 'scale': -1}
],
'field_name_aliases': [
    {'field_name': 'DISTRICT', 'alias': 'DISTRICT'},
    {'field_name': 'POPULATION', 'alias': 'POPULATION'},
    {'field_name': 'COUNTRYCODE', 'alias': 'COUNTRYCODE'},
    {'field_name': 'ID', 'alias': 'ID'},
    {'field_name': 'NAME', 'alias': 'NAME'}
],
"""


def _columns_from_entity(entity):
    columns = []

    query_fields = entity.get("query_fields")
    field_name_aliases = entity.get("field_name_aliases")

    for query_field in query_fields:
        """Extract field properties"""
        col_name = query_field.get("name")
        col_type = query_field.get("type_name")

        is_key_field:bool = query_field.get("is_key_field")
        is_key = 'true' if is_key_field else 'false'

        is_not_null:bool = query_field.get("is_notnull_constraint_field")
        is_nullable = 'false' if is_not_null else 'true'

        precision = query_field.get("precision")
        scale = query_field.get("scale")

        """extract alias"""
        col_alias = ""
        for field_name_alias in field_name_aliases:
            field_name = field_name_alias.get("field_name")
            if field_name == col_name:
                col_alias = field_name_alias.get("alias")
                break

        column = {
            "name":         col_name,
            "alias":        col_alias,
            "type":         col_type,
            "is_key":       is_key,
            "is_nullable":  is_nullable,
            "precision":    precision,
            "scale":        scale,
        }

        columns.append(column)

    return columns


#
# The [IgniteContext] manages requests to an Ignite cluster
# leveraging pyignite
#

def clean_stmt(stmt):
    """
    Apache Superset tests a specified schema, table & field
    definition with SQL database query. The built SQL, however,
    cannot be interpreted by Apache Ignite, as it contains
    the table name extended by the schema: "<schema>"."<table>"
    """
    if "\"SQL_" in stmt:
        """
        The provided SQL statement contains
        a schema reference
        
        SQL_<SCHEMA_NAME>_<TABLE_NAME>
        """
        m = re.search(r"(.*)\"SQL_([A-Z0-9_]+)\"(.*)", stmt)
        if m:
            """The schema name is group(2)"""
            schema_token = "\"SQL_" + m.group(2) + "\"."
            stmt = stmt.replace(schema_token, "")
            """
            Apache Superset uses quotation marks to describe fields;
            these must be replaced also
            """
            stmt = stmt.replace("\"", "")
            return stmt

        else:
            stmt

    else:
        """
        The provided SQL statement does not contain
        any schema reference 
        """
        return stmt


class IgniteContext(object):
    """
    Apache Ignite connection context using the Ignite
    Thin Python client
    """

    def __init__(self,
                 host='127.0.0.1',
                 port=10800,
                 # (optional) sets timeout (in seconds) for each socket operation including
                 # `connect`. 0 means non-blocking mode, which is virtually guaranteed to fail.
                 # Can accept integer or float value. Default is None (blocking mode).
                 timeout=None,
                 # (optional) sets timeout (in seconds) for performing handshake (connection)
                 # with node. Default is 10.0 seconds.
                 handshake_timeout=None,
                 # (optional) set to True if Ignite server uses SSL on its binary connector.
                 # Defaults to use SSL when username and password has been supplied, not to use
                 # SSL otherwise.
                 use_ssl=None,
                 # (optional) SSL version constant from standard `ssl` module. Defaults to TLS v1.2.
                 ssl_version=None,
                 # (optional) ciphers to use. If not provided, `ssl` default ciphers are used.
                 ssl_ciphers=None,
                 # (optional) determines how the remote side certificate is treated:
                 #
                 # * `ssl.CERT_NONE`        − remote certificate is ignored (default),
                 # * `ssl.CERT_OPTIONAL`    − remote certificate will be validated,
                 #
                 # if provided,
                 # * `ssl.CERT_REQUIRED`    − valid remote certificate is required
                 #
                 ssl_cert_reqs=None,
                 # (optional) a path to SSL key file to identify local (client) party
                 ssl_keyfile=None,
                 # (optional) password for SSL key file, can be provided when key file is
                 # encrypted to prevent OpenSSL password prompt
                 ssl_keyfile_password=None,
                 # (optional) a path to ssl certificate file to identify local (client) party.
                 ssl_certfile=None,
                 # (optional) a path to a trusted certificate or a certificate chain.
                 # Required to check the validity of the remote (server-side) certificate
                 ssl_ca_certfile=None,
                 # (optional) user name to authenticate to Ignite cluster
                 username=None,
                 # password to authenticate to Ignite cluster.
                 password=None,
                 ):

        kw_args = {
            'timeout': timeout,
            'handshake_timeout': handshake_timeout,
            'use_ssl': use_ssl,
            'ssl_version': ssl_version,
            'ssl_ciphers': ssl_ciphers,
            'ssl_cert_reqs': ssl_cert_reqs,
            'ssl_keyfile': ssl_keyfile,
            'ssl_keyfile_password': ssl_keyfile_password,
            'ssl_certfile': ssl_certfile,
            'ssl_ca_certfile': ssl_ca_certfile,
            'username': username,
            'password': password
        }

        """The reference to the Ignite Thin client"""
        self.client = Client(**kw_args)
        self.client.connect(host, port)

    def close(self):
        if self.client:
            self.client.close()

    def sql(self, stmt, parameters=None, bulk_parameters=None):
        """
        Execute SQL statement against Apache Ignite cluster.
        """
        if stmt is None:
            return None

        ############################################################
        #
        # GET CACHES
        #
        #############################################################
        if stmt.startswith("GET CACHES"):
            """
            Mimic the response of a schema request as a regular
            database request
            """
            cache_names = self.get_schema_names()
            rows = [[cache_name] for cache_name in cache_names]
            response = {
                'cols': ['name'],
                'rows': rows
            }

            return response

        ############################################################
        #
        # GET TABLES
        #
        #############################################################

        elif stmt.startswith("GET TABLES"):
            schema = ""
            if "FROM" in stmt:
                schema = stmt.split("FROM", 1)[1].strip()

            table_names = self.get_table_names(schema)
            rows = [[table_name] for table_name in table_names]
            response = {
                'cols': ['name'],
                'rows': rows
            }

            return response

        ############################################################
        #
        # GET COLUMNS
        #
        #############################################################

        elif stmt.startswith("GET COLUMNS"):
            """Extract schema from statement"""
            schema = ""
            if "WITH" in stmt:
                schema = stmt.split("WITH", 1)[1].strip()

                phrase = " WITH " + schema
                stmt = stmt.replace(phrase, "")

            """Extract table from statement"""
            table = stmt.split("FROM", 1)[1].strip()

            columns = self.get_columns(table, schema)
            if len(columns) == 0:
                return {'cols': [], 'rows': []}

            rows = []
            for column in columns:
                values = [
                    column.get("name"),
                    column.get("alias"),
                    column.get("type"),
                    column.get("is_key"),
                    column.get("is_nullable"),
                    column.get("precision"),
                    column.get("scale"),
                ]
                rows.append(values)

            response = {
                'cols': ['name', 'alias', 'type', 'is_key', 'is_nullable', 'precision', 'scale'],
                'rows': rows,
            }

            return response

        ############################################################
        #
        # GET COLUMNS
        #
        #############################################################

        elif stmt.startswith("GET KEYS"):
            """Extract schema from statement"""
            schema = ""
            if "WITH" in stmt:
                schema = stmt.split("WITH", 1)[1].strip()

                phrase = " WITH " + schema
                stmt = stmt.replace(phrase, "")

            """Extract table from statement"""
            table = stmt.split("FROM", 1)[1].strip()

            columns = self.get_columns(table, schema)
            if len(columns) == 0:
                return {'cols': [], 'rows': []}

            rows = []
            for column in columns:
                if column.get("is_key") == "true":
                    rows.append([column.get("name")])

            response = {
                'cols': ['name', ],
                'rows': rows,
            }

            return response

        else:
            stmt = clean_stmt(stmt)
            result = self.client.sql(
                stmt,
                #
                # (optional) cursor page size. Default is 1024, which
                # means that client makes one server call per 1024 rows
                #
                page_size=1024,
                #
                # (optional) include field names in result. Default is false
                #
                include_field_names=True)
            """
            The sql method generates a list of columns in the first
            yield. This can be accessed with the __next__ function
            """
            field_names = next(result)

            rows = []
            for values in result:
                rows.append(values)

            response = {
                'cols': field_names,
                'rows': rows
            }
            return response

    def _columns_from_cache(self, table_name, cache_name):

        columns = []

        cfg = self.client.get_cache(cache_name).settings
        if 200 in cfg:
            entities = cfg.get(200)
            for entity in entities:
                tableName = entity.get("table_name")
                if table_name == tableName:
                    columns = _columns_from_entity(entity)
                    break

        return columns

    def get_columns(self, table_name, schema=None):
        """
        Retrieve the cache configuration that refers to
        the provided table_name (and schema)
        """
        columns = []
        cache_names = self.client.get_cache_names()
        if schema:
            """
            Check whether the provided schema refers
            to one of the registered cache names
            """
            is_cache = any(schema in cache_name for cache_name in cache_names)
            if is_cache:
                columns = self._columns_from_cache(table_name, schema)
                """Check whether columns are not empty"""
                if len(columns) != 0:
                    return columns

        """ 
        The provided schema does not exist or the table name does not
        refer to the schema; then, we need to find the matching settings 
        from the provided table name
        """
        for cache_name in cache_names:
            columns = self._columns_from_cache(table_name, cache_name)
            """Check whether columns are not empty"""
            if len(columns) != 0:
                return columns

        return columns

    def get_schema_names(self):
        """
        Retrieve the registered schemas; note, in Apache Ignite
        the cache names refer to the respective schema
        """

        return self.client.get_cache_names()

    def get_table_names(self, schema=None):
        """
        Note: Apache Ignite defines caches (by cache names) and
        each cache contains a list of query entities. Each entity
        refers to a SQL table
        """
        tables = []
        cache_names = self.client.get_cache_names()
        """
        Check whether the schema (name) is one of the extracted
        cache names
        """
        if schema:
            is_cache = any(schema in cache_name for cache_name in cache_names)
            if is_cache:
                """
                Retrieve the respective cache settings and extract
                the associated table name
                """
                cfg = self.client.get_cache(schema).settings
                if 200 in cfg:
                    entities = cfg.get(200)
                    for entity in entities:
                        table_name = entity.get("table_name")
                        tables.append(table_name)
                    return tables
        """
        In case no schema (cache name) is provided, we extract all
        table names from all caches available in Apache Ignite
        """
        for cache_name in cache_names:
            """
            Retrieve cache settings from cache & cache name
            
            The relevant information is contained by settings
            key '200'. This is a list of query entries:

            [
                {
                    'key_type_name': 'SQL_PUBLIC_CITY_5c664bd4_741b_43c1_aad7_541cabc6f7af_KEY',
                    'value_type_name': 'SQL_PUBLIC_CITY_5c664bd4_741b_43c1_aad7_541cabc6f7af',
                    'table_name': 'CITY',
                    'key_field_name': None,
                    'value_field_name': None,
                    'query_fields': [
                        {'name': 'ID', 'type_name': 'java.lang.Integer', 'is_key_field': True, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': -1, 'scale': -1},
                        {'name': 'NAME', 'type_name': 'java.lang.String', 'is_key_field': False, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': 35, 'scale': -1},
                        {'name': 'COUNTRYCODE', 'type_name': 'java.lang.String', 'is_key_field': True, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': 3, 'scale': -1},
                        {'name': 'DISTRICT', 'type_name': 'java.lang.String', 'is_key_field': False, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': 20, 'scale': -1},
                        {'name': 'POPULATION', 'type_name': 'java.lang.Integer', 'is_key_field': False, 'is_notnull_constraint_field': False, 'default_value': None, 'precision': -1, 'scale': -1}
                    ],
                    'field_name_aliases': [
                        {'field_name': 'DISTRICT', 'alias': 'DISTRICT'},
                        {'field_name': 'POPULATION', 'alias': 'POPULATION'},
                        {'field_name': 'COUNTRYCODE', 'alias': 'COUNTRYCODE'},
                        {'field_name': 'ID', 'alias': 'ID'},
                        {'field_name': 'NAME', 'alias': 'NAME'}
                    ],
                    'query_indexes': []
                }
            ]
            """
            cfg = self.client.get_cache(cache_name).settings
            if 200 in cfg:
                entities = cfg.get(200)
                for entity in entities:
                    table_name = entity.get("table_name")
                    tables.append(table_name)

        return tables

    def __repr__(self):
        return '<IgniteClient {0}>'.format(str(self.client))
