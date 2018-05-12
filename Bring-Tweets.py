from pymongo import MongoClient
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

client = MongoClient("localhost",27017)
db = client.Twitchu
UserTweets = db.UserTweets
Users = db.Users

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
        print(dict['tweet'])



#TODO
"""
사용자 목록을 뒤지고, 하나씩 가져온다. 
리트윗된 것을 가져오고, 트윗된 것을 가져온다.

"""

"""
schema를 디자인할 때 고려사항
- 사용자 요구에 따라 디자인
- 객체들을 함께 사용하게 되면 한 document에 합쳐서 사용
- 데이터를 작성할 때 join
"""
