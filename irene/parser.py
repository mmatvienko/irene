#!/usr/bin/env python3

import spacy
from collection import Collection

# have core_parser (takes raw text)
# JSON, CSV, etc will all be subclasses of core_parser
# allow for pre-parsing and serialization/pickling or something

class Core_Parser():
	def __init__(self, file):
		self.file = file
		pass
	def get_collection(self):
		return Collection()
		