# -*- coding: utf-8 -*-
"""
@author: metalcorebear
"""

"""
This library will measure sentiment around specific entities within text.  It is built on NLTK, Spacy, and NRCLex.  Output is a dictionary that can be analyzed further, graphed, formulated into a wordcloud, etc.

https://github.com/explosion/spaCy
https://github.com/nltk
https://github.com/metalcorebear/NRCLex

"""

import os
import nltk
import spacy
from nrclex import NRCLex


nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')

os.system('python -m spacy download en_core_web_sm')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize


class SentiMizer():
    '''
    The SentiMizer class will allow a user to find entities within text and measure sentiment surrounding those entities.
    '''
    def __init__(self):
        self.text = None
        self.entities = None
        self.sentiments = None
        self.sentences = None
        self.affect = None
    
    def load_text(self, text : str):
        self.text = text
        
    def append_text(self, text : str):
        if self.text == None:
            self.text = text
        else:
            self.text = self.text + ' ' + text
    
    def find_entities(self, model="en_core_web_sm", entity_types_of_interest = ['NORP', 'ORG', 'PERSON', 'FAC', 'GPE', 'LOC', 'EVENT']):
        nlp = spacy.load(model)
        entities = nlp(self.text)
        self.entities = dict([(str(x), x.label_) for x in entities.ents if x.label_ in entity_types_of_interest])
        ents = list(self.entities.keys())
        self.sentences = dict()
        sentences = sent_tokenize(self.text)
        for ent in ents:
            sent_list = []
            for sentence in sentences:
                if ent in sentence:
                    sent_list.append(sentence)
            self.sentences.update({ent:' '.join(sent_list)})
            
    def emote(self, entity_type=None):
        if self.text != None:
            if self.entities == None:
                print('Error: Find entities first.')
            # NLTK Vader sentiment scores
            vader = SentimentIntensityAnalyzer()
            self.sentiments = dict()
            self.affect = dict()
            # Filter by entity type
            if entity_type != None:
                filtered_entities = {key:value for (key, value) in self.entities.items() if value == entity_type}
                entity_list = list(filtered_entities.keys())
                filtered_sentences = {key:value for (key, value) in self.sentences.items() if key in entity_list}
            else:
                filtered_sentences = self.sentences
                filtered_entities = self.entities
            for key in filtered_sentences:
                pol = vader.polarity_scores(filtered_sentences[key])
                self.sentiments.update({key:pol['compound']})
            # NRCLex affect scores
            for key in filtered_sentences:
                aff = NRCLex(filtered_sentences[key])
                affect_frequencies = aff.affect_frequencies
                if 'anticip' in affect_frequencies:
                  del affect_frequencies['anticip']
                self.affect.update({key:affect_frequencies})
        else:
            print('Error: No text to analyze.  Load text using the load_text() method.')