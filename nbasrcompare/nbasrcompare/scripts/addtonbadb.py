#class will allow for interaction with mysql database/table
#main functions will be get and set
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from sentence_transformers import SentenceTransformer
from confidential import USERNAME,PASSWORD
class srdb:
    def __init__(self,dbname,collection):
        self.client=MongoClient("mongodb+srv://"+USERNAME+":"+PASSWORD+"@nbascoutingreportdb.f9lpm.mongodb.net/?retryWrites=true&w=majority&appName=nbascoutingreportdb", server_api=ServerApi('1'))
        self.db=self.client[dbname]
        self.collection=self.db[collection]
        self.model=SentenceTransformer("all-mpnet-base-v2")
    def insert(self,playername,s,w,n):
        swn=s+" "+w+" "+n
        playerdict={"playername":playername,"Strengths":s,"Weaknesses":w,"other notes":n,"embedding":self.model.encode(swn).tolist()}
        self.collection.insert_one(playerdict)
    def get(self,playername):
        return None

        

    
