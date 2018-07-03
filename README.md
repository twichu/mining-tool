# Mining tool

## Files
Bring-Tweets.py
몽고 디비가 있는 서버에 접속해, UserTweets 와 Users 컬렉션을 참조하고
Users의 트윗을 가져와 정규 표현식으로 전처리하고 TDM.init()으로 TDM을 초기화한다.
User 하나의 트윗을 분석해 키워드를 추출하고(TDM.twitter_to_keyword(text))
User의 전체 트윗을 분석해 세 개의 키워드를 추출한다( TDM.user_extract_keyword(str_list)).
ForUser가 True로 되어 있을 경우, 몽고 디비의 Users 컬렉션의 키워드를 달고,
False로 되어 있을 경우 UserTweets 컬렉션에 키워드를 단다.

TDM.py
TDM.init() : TDM을 초기화
TDM.twitter_to_keyword(twitter) : 문자열 twitter를 입력으로 받아 키워드를 반환
TDM.user_extract_keyword(twitter_list) : 문자열 리스트 twitter_list를 입력하여 키워드 리스트를 반환

### Shell