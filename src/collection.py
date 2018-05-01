#!/usr/bin/env python3

from spacy.matcher import Matcher
import en_core_web_sm
# make this a global var?
nlp = en_core_web_sm.load()

class Collection:
    def __init__(self, doc = [], data = None):
        self.doc = doc
        self.data = data

    def get_data(self):
        return self.data

    def get_doc(self):
        return self.doc

    def match(self, query):
		#TODO rewrite to handle new query representation
        matcher = Matcher(nlp.vocab)
        pattern = [{'ORTH': query}]
        matcher.add('annoying pattern', None, pattern)
        match = matcher(self.doc)
        total_span = ""
        for match_id, start, end in match:
            string_id = nlp.vocab.strings[match_id]
            span = self.doc[start:end]
            total_span += str(span)
            total_span += "\n"
        return total_span