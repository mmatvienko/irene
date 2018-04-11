#!/usr/bin/env python3

from parser import Core_Parser
from collection import Collection

class Query_Engine:
	def __init__(self, file):
		# random var for now
		self.data = []
		self.file = file
		parser = Core_Parser(file)
		self.collection = parser.get_collection()
		
	def search_corp(self, query):
		# probably best if a generator is returned
		self.query = query
		print(" successful query call for ", query)
		return "(use the query on the parser)"