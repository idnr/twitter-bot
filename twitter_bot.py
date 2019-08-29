from twython import Twython, TwythonError
import schedule 
import time 


# You can change the below hashtags, add or remove too.
hashtags = ["#massage", "#mobilemassage", "#losangeles", "#ondemand", "#california"]

def twitter_api():

    consumer_key = "5RoLRKFEvAPL0zI6t3uhCpkTr"
    consumer_secret = "zrmSOrBSE5P9OKakrMRBSMLifCdWMRHucHy2Qt718mLnKVcnp1"
    access_token = "1126290728785567745-7xWIlojISlVFAXiuEpDi1lLPWgCOBc"
    access_token_secret = "x7pIKhayb1iBse1JvwEbvgggeTmhzrFeAug7tYE1Luwzq"
    return Twython(consumer_key, consumer_secret, access_token, access_token_secret)

def retweet():

    api = twitter_api()
    
    for tag in hashtags: 
        search_results = api.search(q=tag + "-filter:retweets AND -filter:replies", count=5, lang="en", result_type="recent")
        try:
            for tweet in search_results["statuses"]:
                api.retweet(id = tweet["id_str"])
                print(tweet['text'])
                print("\n")
                print('Retweeted!')
                time.sleep(30)
        except TwythonError as e:
            print("something went wrong because", e)

def auto_follow():

    api = twitter_api()
    for tag in hashtags: 
        search_results = api.search(q=tag + "-filter:retweets AND -filter:replies", count=5, lang="en", result_type="recent")
        try:
            for tweet in search_results["statuses"]:
                user_id = tweet.get('user').get('id')
                handle = tweet.get('user').get('screen_name')
                api.create_friendship(id = user_id)
                print(tweet.get('text'))
                print(f'User {handle} followed')
                time.sleep(60)
        except TwythonError as e:
            print("something went wrong because", e)

schedule.every(30).minutes.do(retweet)
schedule.every().hour.do(auto_follow)

if __name__ == "__main__":
    print("[+] Retweeting keywords/hashtags every 30 minutes...")
    print("[+] Following any that tweet keywords/hashtags every hour...")
    while True:
        schedule.run_pending()
        time.sleep(1)
# auto_follow()
