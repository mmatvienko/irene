#!/usr/bin/env python3

from query_engine import QueryEngine

print("file name: ")
file = str(input())

qe = None

if file is '':
    qe = QueryEngine()
else:
    qe = QueryEngine(file)

print("search for: ")
search_term = str(input())

result = qe.search_corp(search_term)
