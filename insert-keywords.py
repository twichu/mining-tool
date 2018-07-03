from pymongo import MongoClient
import urllib.parse

username = urllib.parse.quote_plus('')
password = urllib.parse.quote_plus('')

client = MongoClient('' % (username, password))
db = client.twichu
keywords = db.keywords

f= open('keyword_set', 'rt', encoding="UTF-8")
while True:
    key = f.readline()
    key = key.split('\n')[0]

    if not key:
        break
    keywords.insert_one(
        {
            'keyword':key
        }
    )


f.close()
