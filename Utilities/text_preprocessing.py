# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:12:36 2019
@author: louriki
"""

# Text preprocessing with spaCy and NLTK

import re
import time
import en_core_web_sm
from nltk.stem import WordNetLemmatizer 
from api import settings
from api.rest.utils import loader

def get_cleaned_term(term):
    """
    Returns the term without punctuation and numbers and the list of words composing this term. 
    """
    new_term = term.lower()
    new_term = re.sub(r'[^\w\s]', ' ', new_term)
    new_term = re.sub(r'[0-9]+', ' ', new_term)
    return new_term

def preprocess(term):
    """ Pre-processes one G&S term
    
    For one given term: lowercase transformation, punctuation and number removal, 
    tokenization, stopwords removal and lemmatization
    
    Input:
        -- term: the term we want to preprocess
    
    Output:
        -- final_term: the preprocessed term as a list
    
    """
    start = time.time()
    nlp_model = loader.get_language_model()
    new_term = get_cleaned_term(term)
    
    #Input the term in the model
    doc = nlp_model(new_term)

    #For each token (word), retrieve the result of the lemmatization for this token
    final_term = []
    set_words = settings.STOPWORDS
    for token in doc:
        if token.text not in set_words and not token.text.isspace():
            final_term.append(token.lemma_)

    duration = time.time()-start

    return final_term, duration

def create_wordgram(query, n):
    """ Create a list of n word-grams based on a query
    
    Input:
        -- query: the term we want to split into n word-grams
        -- n: the size of the word-grams
    
    Output:
        -- List of strings containing each word-grams
    

    Example:
        - query = "How does the algorithm work"
        - n = 3

        sequences = [['How', 'does', 'the', 'algorithm', 'work'], 
                     ['does', 'the', 'algorithm', 'work'],
                     ['the', 'algorithm', 'work']

        list(ngrams) = [('How','does','the'), ('does', 'the', 'algorithm'), ('the', 'algorithm', 'work')]
    """
    sequences = [query[i:] for i in range(n)]
    ngrams = zip(*sequences)

    return [" ".join(ngram) for ngram in ngrams]


def preprocess_nltk(term):
    """ Pre-processes one G&S term
    
    For one given term: lowercase transformation, punctuation and number removal, 
    tokenization, stopwords removal and lemmatization
    
    Input:
        -- term: the term we want to preprocess
    
    Output:
        -- final_term: the preprocessed term as a list
    
    """
    new_term = get_cleaned_term(term)
    
    tmp = word_tokenize(new_term)
    final_term = []
    set_words = settings.STOPWORDS
    for word in tmp:
        if word not in set_words and word != ' ':
            wnl = WordNetLemmatizer()
            word = wnl.lemmatize(word)
            final_term.append(word)

    return final_term

def get_lemma(term):
    """
    Returns the words obtained with get_words of the term in parameter preprocessed with spacy.
    """
    list_lemma = []
    new_term = get_cleaned_term(term)
    doc = self.nlp_model(new_term)
    for token in doc:
        if token.text not in self.set_words and token.text != ' ':
            list_lemma.append(token.lemma_)
    return list_lemma
