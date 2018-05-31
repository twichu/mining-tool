from pymongo import MongoClient
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import re

client = MongoClient("localhost",27017)
db = client.Twitchu
UserTweets = db.UserTweets
Users = db.Users
p = re.compile(r'https?://.+', re.DOTALL)
g = re.compile(r'@\S+\s')
chinese = re.compile(u'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', re.UNICODE)
japanese = re.compile(u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]', re.UNICODE)

UserCursor = Users.find({})

for UserDocument in UserCursor:
    dict = dumps(UserDocument)
    dict = json.loads(dict)
    UserObjectId = ObjectId(dict['_id']['$oid'])
    UserTweetsCursor = UserTweets.find({'UserObjectId': ObjectId(UserObjectId)})
    print("___________________________________________________________")
    for UserTweetsDocument in UserTweetsCursor:
        dict = dumps(UserTweetsDocument)
        dict = json.loads(dict)
        httpText = p.search(dict["tweet"])
        atText = g.search(dict["tweet"])

        if httpText:
            dict['tweet'] = dict['tweet'].replace(httpText.group(),'')

        if atText:
            dict['tweet'] = dict['tweet'].replace(atText.group(),'')

        text = re.sub(chinese, '', dict['tweet'])
        text = re.sub(japanese, '', dict['tweet'])

        print(text)

#TODO

