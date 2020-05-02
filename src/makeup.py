
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
    logging.info('Profile name has been changed for "'+name+'" 🦄')


def change_description(description):
    makeup.change_profile_description(description)
    logging.info('Profile description has been changed for "'+description+'" 🦄')


def change_banner_picture(path):
    makeup.change_banner_picture(path)
    logging.info('Profile banner has been replaced by "'+path+'" 🦄')


def change_profile_picture(path):
    makeup.change_profile_picture(path)
    logging.info('Profile picture has been replaced by "'+path+'" 🦄')


# status
schedule.every().day.at("07:30").do(change_display_name, name='Nicolas Dupont ☕')
schedule.every().day.at("08:30").do(change_display_name, name='Nicolas Dupont 💻')
schedule.every().day.at("19:00").do(change_display_name, name='Nicolas Dupont 📝')

# banner
schedule.every().day.at("06:30").do(change_banner_picture, path='config/images/banner-night.jpg')
schedule.every().day.at("21:00").do(change_banner_picture, path='config/images/banner-morning.jpg')

# profile
schedule.every().friday.at("18:30").do(change_profile_picture, path='config/images/profile-weekend.jpg')
schedule.every().monday.at("07:30").do(change_profile_picture, path='config/images/profile-week.jpg')

# description
week_description = "Co-founder and CPO at @akeneopim\
\n❤️ crafting products to create value for users and businesses\
\n💬 about #product, #engineering, #teamwork, #learnings"
weekend_description = "Co-founder and CPO at @akeneopim\
\n❤️ crafting products to create value for users and businesses\
\n💬 about #product, #engineering, #indiehacker"
schedule.every().friday.at("18:30").do(change_description, description=week_description)
schedule.every().monday.at("07:30").do(change_description, description=weekend_description)


while True:
    schedule.run_pending()
    time.sleep(1)
