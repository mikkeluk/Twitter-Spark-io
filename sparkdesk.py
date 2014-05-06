#Twitter settings
import tweepy
consumer_key = "xxxxx"
consumer_secret = "xxxxx"
access_token= "xxxxx"
access_token_secret = "xxxxx"

#MySQL DB settings
import pymysql
db_host_name = "127.0.0.1"
db_host_port = 3306
db_user = "root"
db_password = ""
db_db = "xxxxx"
db_twitter_table = "twitter"


conn = pymysql.connect(host=db_host_name, port=db_host_port, user=db_user,  passwd=db_password, db=db_db)
cur = conn.cursor()

def get_live_twitter_followers():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    user = api.get_user('coinbench')
    return str(user.followers_count) 

def update_followers(id, new_count):
    cur.execute('UPDATE '+db_twitter_table+' SET twittercount='+new_count+' WHERE id='+id)    
    conn.commit()
    
    
def get_last_known_followers():
    cur = conn.cursor()
    cur.execute("SELECT id, twittercount FROM "+db_twitter_table)
    row = cur.fetchone()
    twitterfollowers = row[1]
    type(twitterfollowers)
    return str(twitterfollowers)


def run():
    db_no_followers = int(get_last_known_followers())
    actual_no_followers = int(get_live_twitter_followers())

    if(db_no_followers>actual_no_followers):
        #lost some followers :(  
        update_followers("1", get_live_twitter_followers())
        amountChangedBy =  db_no_followers - actual_no_followers
        #HIT THE LIGHTS!!!
        #sparkLight(amountChangedBy)
    
    if(db_no_followers<actual_no_followers):
        #gained some followers :D  
        update_followers("1", get_live_twitter_followers())
        amountChangedBy = actual_no_followers - db_no_followers
        #HIT THE LIGHTS!!!
        #sparkLight(amountChangedBy) 
    conn.close()
run()