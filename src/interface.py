#!/usr/bin/env python3

from query_engine import Query_Engine

print("file name: ")
file = str(input())

qe = None

if file is '':
    qe = Query_Engine()
else:
    qe = Query_Engine(file)

print("search for: ")
search_term = str(input())

result = qe.search_corp(search_term)
