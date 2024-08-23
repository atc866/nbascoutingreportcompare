from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from .scripts.addtonbadb import srdb
import json
from .secrets import USERNAME, PASSWORD, API_KEY
dbconnection=srdb('localhost',USERNAME,PASSWORD,'nbascoutingreports')
class nbasrcomparedbview(APIView):
    @csrf_exempt
    @api_view(['POST'])
    def get(request):
        print("get")
        if request.method=='POST':
            print(request)
            data = json.loads(request.body)
            print("data",data)
        #dbconnection.get(data['player1name'])
        #dbconnection.get(data['player2name'])

        return Response({"comparison":str(data)},status=status.HTTP_200_OK)
