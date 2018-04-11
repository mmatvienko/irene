#!/usr/bin/env python3

import spacy
import en_core_web_sm
from spacy import displacy
nlp = en_core_web_sm.load()

# tags from https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
tags = {}
tags["DT"] = "determiner"
tags["JJ"] = "adjective"
tags["NN"] = "noun"
tags["VBD"] = "verb of past tense"
tags["IN"] =  "preposition"

doc = nlp(u'the quick brown fox jumped over the lazy dog')

for token in doc:
    print("'",token.text,"' is a ", tags[token.tag_])

print("would you like to see a dank chart? (y/n)")
choice = str(input())
if choice == "y":
	# display at localhost:5000
	displacy.serve(doc, style='dep')
else:
	print("sucks to suck")