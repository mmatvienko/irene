#!/usr/bin/env python3

import spacy
import en_core_web_sm
from spacy import displacy
nlp = en_core_web_sm.load()

doc = nlp(u'the quick brown fox jumped over the lazy dog')

for token in doc:
    print(token.text," is a ", token.tag_, " and depends on " , token.dep_)

# display at localhost:5000
displacy.serve(doc, style='dep')

# have core_parser (takes raw text)
# JSON, CSV, etc will all be subclasses of core_parser
# allow for pre-parsing and serialization/pickling or something

class Core_Parser():
	def __init__(self):
		pass
	