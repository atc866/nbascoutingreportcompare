from scrape import scrapePlayer
from addtonbadb import srdb

from secrets import USERNAME, PASSWORD, API_KEY
import google.generativeai as genai
addtodb=srdb('localhost',USERNAME,PASSWORD,'nbascoutingreports')
#scrapecurry=scrapePlayer('https://www.nbadraft.net/players/stephen-curry/')
#scrapecurry.getStrength()
def addplayertodb(scrapeplayer):
    addtodb.set("Stephen Curry",scrapeplayer.getStrength(),scrapeplayer.getWeaknesses(),scrapeplayer.getOtherNotes())
#addplayertodb(scrapecurry)
#addtodb.commit()
#addtodb.close()
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
curry=addtodb.get("Stephen Curry")
irving=addtodb.get("Kyrie Irving")
#print(curry)
#print(irving)
response = model.generate_content(f"Given the scouting report that has the strenghts, weaknesses, and notes in {curry} and the scouting report that has the strengths, weaknesses, and notes in {irving}, please give me some similarities and differences in these two prospects")
response = response.text
print("response ",response)
#testing stuff