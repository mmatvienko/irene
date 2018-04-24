#!/usr/bin/env python3

import spacy
from collection import Collection
import en_core_web_sm
import json

# have core_parser (takes raw text)
# JSON, CSV, etc will all be subclasses of core_parser
# allow for pre-parsing and serialization/pickling or something

class Core_Parser():
	def __init__(self, file):
		self.file = file
		pass
	def get_collection(self):
		return Collection()

class JSON_Parser():
	def __init__(self,file):
		self.file = file
		data = json.load(open(file))
		complaints = [complaint["Summary"].lower() for complaint in data["Results"]]
		corpus = " ".join(complaints)
		self.corpus = corpus

	def get_collection(self):
		nlp = en_core_web_sm.load()
		return Collection(nlp(self.corpus), None)