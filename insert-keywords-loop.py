from pymongo import MongoClient
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import re
import TDM
import urllib.parse

username = urllib.parse.quote_plus('optlab_root')
password = urllib.parse.quote_plus('optlab811!')

client = MongoClient('mongodb://%s:%s@223.194.46.33:2701' % (username, password))
db = client.twichu
UserTweets = db.userstweets
Users = db.users
Tweets = db.tweets
p = re.compile(r'https?://.+', re.DOTALL)
g = re.compile(r'@\S+\s')
chinese = re.compile(u'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', re.UNICODE)
japanese = re.compile(u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]', re.UNICODE)
# while True:
UserTweetsCursor = UserTweets.find({})
TweetsCursor = Tweets.find({})
TDM.init()

for TweetDocument in TweetsCursor:
    dict = dumps(TweetDocument)
    dict = json.loads(dict)
    if dict['isAnalyzing'] == True:
        Tweets.update_one(
            {'_id': ObjectId(dict['_id']['$oid'])},
            {
                '$set': {
                    'cate_keyword': TDM.twitter_to_keyword(dict['tweet']),
                    'isAnalyzing': False
                }
            }, upsert=False
        )
# 트렌드를 순회하는 부분

for UserTweetDocument in UserTweetsCursor:
    dict = dumps(UserTweetDocument)
    dict = json.loads(dict)
    str_list = []
    if dict['is_analyzing']== True:
        for i in range(0,100):
            try:
                str_list.append(dict['tweets'][i]['text'])
            except IndexError:
                break
        for i in range(0, 100):
            try:
                str_list.append(dict['retweets'][i]['text'])
            except IndexError:
                break

        UserTweets.update_one(
            {'_id':ObjectId(dict['_id']['$oid'])},
            {
                '$set':{
                    'is_analyzing':False
                }
            }, upsert=False
        )

        keywords = TDM.user_extract_keyword(str_list)
        # keywords는 사용자의 키워드 3개를 가지고 있는 리스트
        print(keywords)
        UserCursor = Users.find({
            '_id' : ObjectId(dict['user_id'])
        })
        print(UserCursor)
        for UserDocument in UserCursor:
            keywords = keywords + dict['keywords']
            print(dict['keywords'])
            print(keywords)
            keywords_set = set(keywords)

            Users.update_one(
                {'_id': ObjectId(dict['user_id'])},
                {
                    '$set': {
                        'is_analyzing': False,
                        'keywords': list(keywords_set)
                    }
                }, upsert=False
            )

# 유저와 유저 트윗을 순회하는 부분