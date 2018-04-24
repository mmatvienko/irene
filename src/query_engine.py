#!/usr/bin/env python3
import spacy
from parser import *
from collection import Collection

class Query_Engine:
    def __init__(self, file='../data/sample.json'):
        # random var for now
        self.data = []
        self.file = file
        parser = JSON_Parser(file)
        self.collection = parser.get_collection()
		
    def search_corp(self, query):
        # probably best if a generator is returned
        self.query = query
        span = self.collection.query(query)
        # how will we handle different file typers
        print(" successful query call for ", query)
        print(span)
        return "(use the query on the parser)"