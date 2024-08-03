from scrape import scrapePlayer
kyrie=scrapePlayer("https://www.nbadraft.net/players/kyrie-irving/")
print(kyrie.getStrength())
print(kyrie.getWeaknesses())
print(kyrie.getOtherNotes())