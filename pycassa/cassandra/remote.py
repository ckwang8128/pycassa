#!/usr/bin/env python
#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from __future__ import print_function
from __future__ import absolute_import

import os
import sys


from . import Cassandra
from . import ttypes

from thrift.util.remote import Function, Remote
FUNCTIONS = {
    'login': Function('login', 'void', [('AuthenticationRequest', 'auth_request', 'AuthenticationRequest')]),
    'set_keyspace': Function('set_keyspace', 'void', [('string', 'keyspace', 'string')]),
    'get': Function('get', 'ColumnOrSuperColumn', [('string', 'key', 'string'), ('ColumnPath', 'column_path', 'ColumnPath'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'get_slice': Function('get_slice', 'list<ColumnOrSuperColumn>', [('string', 'key', 'string'), ('ColumnParent', 'column_parent', 'ColumnParent'), ('SlicePredicate', 'predicate', 'SlicePredicate'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'get_count': Function('get_count', 'i32', [('string', 'key', 'string'), ('ColumnParent', 'column_parent', 'ColumnParent'), ('SlicePredicate', 'predicate', 'SlicePredicate'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'multiget_slice': Function('multiget_slice', 'map<string, list<ColumnOrSuperColumn>>', [('list<string>', 'keys', 'list<string>'), ('ColumnParent', 'column_parent', 'ColumnParent'), ('SlicePredicate', 'predicate', 'SlicePredicate'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'multiget_count': Function('multiget_count', 'map<string, i32>', [('list<string>', 'keys', 'list<string>'), ('ColumnParent', 'column_parent', 'ColumnParent'), ('SlicePredicate', 'predicate', 'SlicePredicate'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'get_range_slices': Function('get_range_slices', 'list<KeySlice>', [('ColumnParent', 'column_parent', 'ColumnParent'), ('SlicePredicate', 'predicate', 'SlicePredicate'), ('KeyRange', 'range', 'KeyRange'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'get_paged_slice': Function('get_paged_slice', 'list<KeySlice>', [('string', 'column_family', 'string'), ('KeyRange', 'range', 'KeyRange'), ('string', 'start_column', 'string'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'get_indexed_slices': Function('get_indexed_slices', 'list<KeySlice>', [('ColumnParent', 'column_parent', 'ColumnParent'), ('IndexClause', 'index_clause', 'IndexClause'), ('SlicePredicate', 'column_predicate', 'SlicePredicate'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'insert': Function('insert', 'void', [('string', 'key', 'string'), ('ColumnParent', 'column_parent', 'ColumnParent'), ('Column', 'column', 'Column'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'add': Function('add', 'void', [('string', 'key', 'string'), ('ColumnParent', 'column_parent', 'ColumnParent'), ('CounterColumn', 'column', 'CounterColumn'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'remove': Function('remove', 'void', [('string', 'key', 'string'), ('ColumnPath', 'column_path', 'ColumnPath'), ('i64', 'timestamp', 'i64'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'remove_counter': Function('remove_counter', 'void', [('string', 'key', 'string'), ('ColumnPath', 'path', 'ColumnPath'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'batch_mutate': Function('batch_mutate', 'void', [('map<string, map<string, list<Mutation>>>', 'mutation_map', 'map<string, map<string, list<Mutation>>>'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'atomic_batch_mutate': Function('atomic_batch_mutate', 'void', [('map<string, map<string, list<Mutation>>>', 'mutation_map', 'map<string, map<string, list<Mutation>>>'), ('ConsistencyLevel', 'consistency_level', 'ConsistencyLevel')]),
    'truncate': Function('truncate', 'void', [('string', 'cfname', 'string')]),
    'describe_schema_versions': Function('describe_schema_versions', 'map<string, list<string>>', []),
    'describe_keyspaces': Function('describe_keyspaces', 'list<KsDef>', []),
    'describe_cluster_name': Function('describe_cluster_name', 'string', []),
    'describe_version': Function('describe_version', 'string', []),
    'describe_ring': Function('describe_ring', 'list<TokenRange>', [('string', 'keyspace', 'string')]),
    'describe_token_map': Function('describe_token_map', 'map<string, string>', []),
    'describe_partitioner': Function('describe_partitioner', 'string', []),
    'describe_snitch': Function('describe_snitch', 'string', []),
    'describe_keyspace': Function('describe_keyspace', 'KsDef', [('string', 'keyspace', 'string')]),
    'describe_splits': Function('describe_splits', 'list<string>', [('string', 'cfName', 'string'), ('string', 'start_token', 'string'), ('string', 'end_token', 'string'), ('i32', 'keys_per_split', 'i32')]),
    'trace_next_query': Function('trace_next_query', 'string', []),
    'describe_splits_ex': Function('describe_splits_ex', 'list<CfSplit>', [('string', 'cfName', 'string'), ('string', 'start_token', 'string'), ('string', 'end_token', 'string'), ('i32', 'keys_per_split', 'i32')]),
    'system_add_column_family': Function('system_add_column_family', 'string', [('CfDef', 'cf_def', 'CfDef')]),
    'system_drop_column_family': Function('system_drop_column_family', 'string', [('string', 'column_family', 'string')]),
    'system_add_keyspace': Function('system_add_keyspace', 'string', [('KsDef', 'ks_def', 'KsDef')]),
    'system_drop_keyspace': Function('system_drop_keyspace', 'string', [('string', 'keyspace', 'string')]),
    'system_update_keyspace': Function('system_update_keyspace', 'string', [('KsDef', 'ks_def', 'KsDef')]),
    'system_update_column_family': Function('system_update_column_family', 'string', [('CfDef', 'cf_def', 'CfDef')]),
    'execute_cql_query': Function('execute_cql_query', 'CqlResult', [('string', 'query', 'string'), ('Compression', 'compression', 'Compression')]),
    'execute_cql3_query': Function('execute_cql3_query', 'CqlResult', [('string', 'query', 'string'), ('Compression', 'compression', 'Compression'), ('ConsistencyLevel', 'consistency', 'ConsistencyLevel')]),
    'prepare_cql_query': Function('prepare_cql_query', 'CqlPreparedResult', [('string', 'query', 'string'), ('Compression', 'compression', 'Compression')]),
    'prepare_cql3_query': Function('prepare_cql3_query', 'CqlPreparedResult', [('string', 'query', 'string'), ('Compression', 'compression', 'Compression')]),
    'execute_prepared_cql_query': Function('execute_prepared_cql_query', 'CqlResult', [('i32', 'itemId', 'i32'), ('list<string>', 'values', 'list<string>')]),
    'execute_prepared_cql3_query': Function('execute_prepared_cql3_query', 'CqlResult', [('i32', 'itemId', 'i32'), ('list<string>', 'values', 'list<string>'), ('ConsistencyLevel', 'consistency', 'ConsistencyLevel')]),
    'set_cql_version': Function('set_cql_version', 'void', [('string', 'version', 'string')]),
}

if __name__ == '__main__':
    Remote.run(FUNCTIONS, Cassandra, ttypes, sys.argv, default_port=9090)
