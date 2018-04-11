#!/usr/bin/env python3

from parser import Core_Parser

class Query_Engine:
	def __init__(self):
		# random var for now
		self.data = []
	def search_corp(self, query):
		# probably best if a generator is returned
		self.query = query
		print(" successful query call for ", query)
		return "[insert dank data]"