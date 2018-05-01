#!/usr/bin/env python3
import spacy
from parser import *
from collection import Collection
from input import *

class Query_Engine:
    def __init__(self, file='../data/sample.json'):
        # random var for now
        self.data = []
        self.file = file
        parser = JSON_Parser(file)
        self.collection = parser.get_collection()
		handler = input.Input_Handler()
		
    def search_corp(self, str_query):
        # probably best if a generator is returned
        self.last_query = str_query
		processed_query = handler.process_query(str_query)
        span = self.collection.match(processed_query)
        # how will we handle different file typers
        print(" successful query call for ", query)
        print(span)
        return "(use the query on the parser)"
	