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
	lower_case = str(complaint["Summary"]).lower()
	print(lower_case)
	docs.append( nlp( lower_case ) )

matcher = Matcher(nlp.vocab)
pattern = [{'ORTH': 'reasonable'}]
# change pattern to have specfic
matcher.add('annoying pattern', None, pattern)
doc = docs[7]
match = matcher(doc)
for match_id, start, end in match:
    string_id = nlp.vocab.strings[match_id]  # 'HelloWorld'
    span = doc[start:end]                    # the matched span
    print(span)
    