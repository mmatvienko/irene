#!/usr/bin/env python3

import spacy
from spacy import displacy
from spacy.matcher import Matcher
import en_core_web_sm
import re
nlp = en_core_web_sm.load()

doc = nlp(u'The US president is also know as the United States president these days.')

us_regex = r'[Uu](nited)? ?[Ss](tates)?'
us_flag = lambda text: bool(re.compile(us_regex).match(text))
is_us = nlp.vocab.add_flag(us_flag)

matcher = Matcher(nlp.vocab)
us_president_pattern = [
    {is_us: True},
    {'LOWER': 'president', 'TAG': 'NN'}
]

matcher.add('regex test', None, us_president_pattern)

print('Printing matches:')
match = matcher(doc)
for match_id, start, end in match:
	span = doc[start:end]
	print("Found \"{}\" at range ({},{})".format(span,start,end))

# Note that multiple words cannot be matched
    
print("Display? (y/n)")
choice = str(input())
if choice == "y":
	# display at localhost:5000
	displacy.serve(doc, style='dep')