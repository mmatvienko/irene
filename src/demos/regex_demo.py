#!/usr/bin/env python3

import spacy
from spacy import displacy
from spacy.matcher import Matcher
import en_core_web_sm
import re
nlp = en_core_web_sm.load()

doc = nlp('The US president is also know as the United States president these days.')

matcher = Matcher(nlp.vocab)
us_president_pattern = [
    {'REGEX': '^([Uu](\\.?|nited) ?[Ss](\\.?|tates)'},
    {'LOWER': 'president'}
]

matcher.add('regex test', None, us_president_pattern)

print('Printing matches:')
match = matcher(doc)
for match_id, start, end in match:
	span = doc[start:end]
	print(span)
	print (start)
	print(end)

print("Display? (y/n)")
choice = str(input())
if choice == "y":
	# display at localhost:5000
	displacy.serve(doc, style='dep')