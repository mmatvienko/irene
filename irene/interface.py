#!/usr/bin/env python3

from query_engine import Query_Engine
qe = Query_Engine()

print("search for: ")
search_term = str(input())

result = qe.search_corp(search_term)