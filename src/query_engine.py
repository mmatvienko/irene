#!/usr/bin/env python3
import spacy

from parser import JsonParser
from collection import Collection
from input import InputHandler


class QueryEngine:
    def __init__(self, file='../data/sample.json'):
        # random var for now
        self.data = []
        self.file = file
        parser = JsonParser(file)
        self.collection = parser.get_collection()
        self.handler = InputHandler()

    def search_corp(self, str_query):
        # probably best if a generator is returned
        self.last_query = str_query
        processed_query = self.handler.process_query(str_query)
        span = self.collection.match(processed_query)
        # how will we handle different file typers
        print("successful query call for ", str_query)
        print(span)
        return "(use the query on the parser)"
