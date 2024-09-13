from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from .scripts.addtonbadb import srdb
import json
from .confidential import USERNAME,PASSWORD,API_KEY
import google.generativeai as genai
dbconnection=srdb("nbasrcompare",USERNAME,PASSWORD,"scoutingreports")
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
        player1data=dbconnection.get(data['player1name'])
        player2data=dbconnection.get(data['player2name'])
        p1=player1data['Strengths']+" "+player1data['Weaknesses']+" "+player1data["other notes"]
        p2=player2data['Strengths']+" "+player2data['Weaknesses']+" "+player2data["other notes"]
        cosinescore=dbconnection.model.similarity(player1data['embedding'],player2data['embedding'])[0]
        response = model.generate_content(f"Given the scouting report that has the strenghts, weaknesses, and notes in {p1} and the scouting report that has the strengths, weaknesses, and notes in {p2}, please give me some similarities and differences in these two prospects")
        response = response.text
        print("response ",response)

        return Response({"comparison":str(response),"score":cosinescore},status=status.HTTP_200_OK)
