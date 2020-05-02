
import schedule
import time
import logging
import tweepy
import configparser
from twitter_makeup import MakeUp
import functools
from datetime import datetime
now = datetime.now()

# load config
config = configparser.ConfigParser()
config.read('config/secrets.ini')

# configure tweepy
auth = tweepy.OAuthHandler(config['CREDENTIALS']['consumer_key'], config['CREDENTIALS']['consumer_secret'])
auth.set_access_token(config['CREDENTIALS']['access_token'], config['CREDENTIALS']['access_secret'])
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
makeup = MakeUp(api)

# enable logging
logging.basicConfig(filename='log/makeup.log',level=logging.INFO)


# catch exceptions on jobs
def catch_exceptions(cancel_on_failure=False):
    def catch_exceptions_decorator(job_func):
        @functools.wraps(job_func)
        def wrapper(*args, **kwargs):
            try:
                return job_func(*args, **kwargs)
            except:
                import traceback
                print(traceback.format_exc())
                if cancel_on_failure:
                    return schedule.CancelJob
        return wrapper
    return catch_exceptions_decorator


@catch_exceptions(cancel_on_failure=True)
def change_display_name(name):
    makeup.change_profile_name(name)
    logging.info('Profile name has been changed for "'+name+'" 🦄')
    print('Profile name has been changed for "'+name+'" 🦄')


@catch_exceptions(cancel_on_failure=True)
def change_description(description):
    makeup.change_profile_description(description)
    logging.info('Profile description has been changed for "'+description+'" 🦄')
    print('Profile description has been changed for "'+description+'" 🦄')


@catch_exceptions(cancel_on_failure=True)
def change_banner_picture(path):
    makeup.change_banner_picture(path)
    logging.info('Profile banner has been replaced by "'+path+'" 🦄')
    print('Profile banner has been replaced by "'+path+'" 🦄')


@catch_exceptions(cancel_on_failure=True)
def change_profile_picture(path):
    makeup.change_profile_picture(path)
    logging.info('Profile picture has been replaced by "'+path+'" 🦄')
    print('Profile picture has been replaced by "'+path+'" 🦄')


# status
schedule.every().day.at("07:30").do(change_display_name, name='Nicolas Dupont ☕')
schedule.every().day.at("08:30").do(change_display_name, name='Nicolas Dupont 💻')
schedule.every().day.at("13:39").do(change_display_name, name='Nicolas Dupont ☕')
schedule.every().day.at("13:55").do(change_display_name, name='Nicolas Dupont 💻')
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


print('Launch the scheduler ⏲️')
for job in schedule.jobs:
    print(job)
current_time = now.strftime("%H:%M:%S")
print("Current time =", current_time)


while True:
    schedule.run_pending()
    time.sleep(1)
