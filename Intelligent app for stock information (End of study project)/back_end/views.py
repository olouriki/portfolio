import json
from bson import json_util
from django.shortcuts import get_object_or_404
from models.models import Model
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from .serializers import ModelSerializer
from ..apps import AnalysisSentiment
from ..apps import ConnexionDB
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from ..apps import printOmar


@permission_classes((permissions.AllowAny,))
class Senti(APIView):

    def get(self, request):
        if request.method == 'GET':
            # sentence is the query we want to get the prediction for
            text = request.GET.get("text")
            print('QA pred')
            response = AnalysisSentiment.modelVador.predict(
                text)
            print(response)
            return JsonResponse(response, safe=False)


@permission_classes((permissions.AllowAny,))
class Article(APIView):
    def get(self, request):
        if request.method == 'GET':
            text = request.GET.get("article_id")
            article =   ConnexionDB.db.article.find_one()
            res = {'body' : article["body"]}
            return JsonResponse(res, safe=False)


@permission_classes((permissions.AllowAny,))
class testOmar(APIView):

    def get(self, request):
            # sentence is the query we want to get the prediction for
            response = printOmar.modelOmar.printMsg("omar test test")
            res = {'rep' : response
            }
            return JsonResponse(res, safe=False)


@permission_classes((permissions.AllowAny,))
class Tweet(APIView):

    def get(self, request):
        if request.method == 'GET':
            # sentence is the query we want to get the prediction for
            response = Tweet.last_tweet
            print(response)
            return JsonResponse(response, safe=False)


@permission_classes((permissions.AllowAny,))
class TEST(APIView):

    def get(self, request):
        print('test pred')

        return JsonResponse("OK TEST CALL API", safe=False)
    

@permission_classes((permissions.AllowAny,))
class TweetStream(APIView):
    def get(self, request):
        if request.method == 'GET':
            # sentence is the query we want to get the prediction for
            tweet_1 =   ConnexionDB.posts.find_one()
            nb_tweet =  ConnexionDB.posts.count()
            res = {'text' : tweet_1["text"],
                    'nb_tweet' : nb_tweet
            }
            print(res)
            return JsonResponse(res, safe=False)    
