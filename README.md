# mining-tool

TDM을 import 해서 사용을 한다.

TDM.init()으로 TDM 초기값을 초기화 하고 시작을 한다.

TDM.twitter_to_keyword(twitter), user_extract_keyword(twitter_list) 를 사용해서 mining tool을 사용한다.

TDM.twitter_to_keyword(twitter)는 인자로 twitter를 받으면 keyword를 반환을 한다.

user_extract_keyword(twitter_list)는 twitter를 리스트 형태로 인자로 받으면 그 트위터들의 가장 많이 나왔던 keyword 3개를 list형태로 반환을 한다.
