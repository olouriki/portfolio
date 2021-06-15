from bson.objectid import ObjectId
from pymongo import MongoClient
import json
from django.apps import AppConfig
import pickle
import sys

from pymongo import MongoClient

from ml.classifiers.clf_vador import Vader_Sentiment
from ml.classifiers.testOmar import testOmar



class AnalysisVador:
    def __init__(self):
        self.vader = Vader_Sentiment()
        print('... init vador analysis sentiments')

    def predict(self, text):
        res = self.vader.pred(text)
        return res

class AnalysisSentiment:
    modelVador = AnalysisVador()


class testPrintOmar:
    
    def __init__(self):
        print('... init Omar model')
        
    #    self.inst = testOmar()

    def printMsg(self, msg):
        return msg

class printOmar:

    modelOmar = testPrintOmar()


class ConnexionDB:
    client = MongoClient('localhost', 27017)
    db = client.test_database
    collection = db.test_collection
    posts = db.tweet
   
 
