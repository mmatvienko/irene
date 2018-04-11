#!/usr/bin/env python3

import spacy
from spacy import displacy
from spacy.matcher import Matcher
import en_core_web_sm
import json
nlp = en_core_web_sm.load()

# tags from https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
tags = {}
tags["DT"] = "determiner"
tags["JJ"] = "adjective"
tags["NN"] = "noun"
tags["VBD"] = "verb of past tense"
tags["IN"] =  "preposition"

# read in data
data = json.load(open('../../data/sample.json'))

# extract all text
docs = []
for complaint in data["Results"]:
	docs.append(nlp(str(complaint["Summary"]).lower()))

matcher = Matcher(nlp.vocab)
pattern = [{'TAG': 'DT'},{'TAG': 'JJ'},{'TAG': 'NN'}]
# change pattern to have specfic
matcher.add('pronoun verb', None, pattern)

matches = []
for doc in docs:
	matches.append(matcher(doc))

for match in matches:
	for match_id, start, end in match:
	    string_id = nlp.vocab.strings[match_id]  # 'HelloWorld'
	    span = doc[start:end]                    # the matched span
	    print(span)

# for token in doc:
#    print("'",token.text,"' is a ", token.tag_)

fox = nlp(u'the quick brown fox, jumped over the lazy dog')

print("would you like to see a dank dep. chart? (y/n)")
choice = str(input())
if choice == "y":
	# display at localhost:5000
	displacy.serve(fox, style='dep')
else:
	print("sucks to suck")
