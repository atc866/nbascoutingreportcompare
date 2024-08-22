from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
import json
class nbasrcomparedbview(APIView):
    @csrf_exempt
    def get(request):
        print("get")
        if request.method=='POST':
            print(request)
            data = json.loads(request.body)
            print("data",data)
