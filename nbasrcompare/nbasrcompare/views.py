from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from .scripts.addtonbadb import srdb
import json
from .secrets import USERNAME, PASSWORD, API_KEY
import google.generativeai as genai
dbconnection=srdb('localhost',USERNAME,PASSWORD,'nbascoutingreports')
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
class nbasrcomparedbview(APIView):
    @csrf_exempt
    @api_view(['POST'])
    def get(request):
        print("get")
        if request.method=='POST':
            print(request)
            data = json.loads(request.body)
            print("data",data)
        p1=dbconnection.get(data['player1name'])
        p2=dbconnection.get(data['player2name'])
        response = model.generate_content(f"Given the scouting report that has the strenghts, weaknesses, and notes in {p1} and the scouting report that has the strengths, weaknesses, and notes in {p2}, please give me some similarities and differences in these two prospects")
        response = response.text
        print("response ",response)

        return Response({"comparison":str(response)},status=status.HTTP_200_OK)
