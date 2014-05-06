
Readme
=============

This script has been made and intended to be used with a Sparkcore to call the Spark.io API based on Twitter events.



Requirements
=========================

In this repo you will find everything you would need to make it work.

This script uses `tweepy` for communicating with Twitter.  This is the only dependancy aside from Python obviously.

```
  pip install tweepy
```


Installation
============
git clone https://github.com/mikkeluk/Twitter-Spark-io

**Specify your Twitter consumer key and consumer secret**
```
consumer_key = "xxxxx"
consumer_secret = "xxxxx"
```

**Specify a valid access token and token secret**
```
access_token= "xxxxx"
access_token_secret = "xxxxx"
```

**MySQL currently used - Specify database settings**
```
db_host_name = "127.0.0.1"
db_host_port = 3306
db_user = "xxx"
db_password = ""
db_db = "xxxxx"
```

**Create table in database**
```
CREATE TABLE `twitter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `twittercount` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
```

Notes
=========================
Plan on adding Zendesk support and Gmail support, hence the database may seem a little overkill currently.
