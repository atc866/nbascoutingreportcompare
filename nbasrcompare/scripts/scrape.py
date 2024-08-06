from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver

class scrapePlayer:
    def __init__(self,playerUrl):
        self.url=playerUrl
        self.driver=webdriver.Firefox()
        self.driver.get(self.url)
        self.page=bs(self.driver.page_source,'html')
    def getStrength(self):
        paragraphs=self.page.find_all('p')
        strengths=[p.text for p in paragraphs if len(p.text)>0 and "Strengths:" in p.text]
        for i in range(len(strengths)):
            strengths[i]=strengths[i].replace("…",".")
            strengths[i]=strengths[i].replace("\xa0","")
        rv=". ".join(strengths)
        return rv

    def getWeaknesses(self):
        paragraphs=self.page.find_all('p')
        weaknesses=[p.text for p in paragraphs if len(p.text)>0 and "Weaknesses:" in p.text]
        for i in range(len(weaknesses)):
            weaknesses[i]=weaknesses[i].replace("…",".")
            weaknesses[i]=weaknesses[i].replace("\xa0","")
        rv=". ".join(weaknesses)
        return rv
    def getOtherNotes(self):
        paragraphs=self.page.find_all('p')
        notes=[p.text for p in paragraphs if len(p.text)>0 and ("Notes:" in p.text or "Overall:" in p.text or "Outlook:" in p.text)]
        for i in range(len(notes)):
            notes[i]=notes[i].replace("…",".")
            notes[i]=notes[i].replace("\xa0","")
        rv=". ".join(notes)
        return rv



