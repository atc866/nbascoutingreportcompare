from scrape import scrapePlayer
from addtonbadb import srdb

from confidential import USERNAME, PASSWORD, API_KEY
import google.generativeai as genai
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
addtodb=srdb("nbasrcompare",USERNAME,PASSWORD,"scoutingreports")
#scrapecurry=scrapePlayer('https://www.nbadraft.net/players/stephen-curry/')
#scrapeirving=scrapePlayer('https://www.nbadraft.net/players/kyrie-irving/')
#scrapemiller=scrapePlayer('https://www.nbadraft.net/players/brandon-miller/')
# scrapegeorge=scrapePlayer('https://www.nbadraft.net/players/paul-george/')
# def addplayertodb(scrapeplayer):
#     addtodb.insert("paul george",scrapeplayer.getStrength(),scrapeplayer.getWeaknesses(),scrapeplayer.getOtherNotes())
# addplayertodb(scrapegeorge)
print(addtodb.get("Paul George"))
