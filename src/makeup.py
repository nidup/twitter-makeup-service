
import logging
import schedule
import time
import tweepy
from twitter_makeup import MakeUp
from secrets import consumer_key, consumer_secret, access_token, access_secret


logging.basicConfig(filename='log/makeup.log',level=logging.INFO)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
makeup = MakeUp(api)


def change_display_name(name):
    makeup.change_profile_name(name)
    logging.info('Profile name has been changed for "'+name+'"')


def change_banner_picture(path):
    makeup.change_banner_picture(path)
    logging.info('Profile banner has been replaced by "'+path+'"')


# status
schedule.every().day.at("07:30").do(change_display_name, name='Nicolas Dupont ☕')
schedule.every().day.at("08:30").do(change_display_name, name='Nicolas Dupont 💻')
schedule.every().day.at("19:00").do(change_display_name, name='Nicolas Dupont 📝')

# banner
schedule.every().hour.at(":57").do(change_banner_picture, path='config/images/banner-night.jpg')
schedule.every().hour.at(":58").do(change_banner_picture, path='config/images/banner-morning.jpg')






while True:
    schedule.run_pending()
    time.sleep(1)
