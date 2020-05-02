# Make up your Twitter Profile! [docker service]

Small service to automate the make up of your twitter profile, from 🐴 to 🦄 !

Based on a scheduler and Twitter API, you can change your profile at any day 📅 or any hour 🕒.

You can see it live on my [Twitter profile](https://twitter.com/duponico) 🐦

## Examples 🦄

Example                                         | Result
----------------------------------------------- | ------------------------------
Change the banner for the day                   | ![alt text](./config/images/banner-morning.jpg "Morning banner")
And the night                                   | ![alt text](./config/images/banner-night.jpg "Night banner")
Change your display name the morning            | Nico ☕
And during the day                              | Nico 💻
And for the night                               | Nico 😴
Change your profile picture the weekend         | ![alt text](./config/images/profile-weekend.jpg "weekend profile")
Change your location when traveling             | Boston
Change your description when attending an event | Currently at #craftconf, let's have a chat 💬

## Install 🐋

Clone the repository:

```
git clone git@github.com:nidup/twitter-makeup-service.git
```

Build the Docker image:

```
docker-compose build
```

## Configure the Credentials 🔐

Twitter Make Up allows to programmatically change your profile **on your behalf**.

To configure it, you need to generate Twitter credentials.

[Follow the Twitter guide (OAuth 1.0a)](https://developer.twitter.com/en/docs/basics/authentication/overview).

Then create a `secrets.ini` file with your credentials in the `config` folder:

```
[CREDENTIALS]
consumer_key = YourConsumerKey
consumer_secret = YourConsumerSecret
access_token = YourAccessToken
access_secret = YourAccessSecret
```

## Configure your Make Up 🐴

Drop your pictures in `config/images`

Edit the file makeup/scheduler.py, here are a few examples:

```python

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
```

*I'll extract the scheduling configuration to make it easier to customize*

## Launch and Enjoy 🦄

```
docker-compose up

Starting twitter_makeup_cli ... done
Attaching to twitter_makeup_cli
twitter_makeup_cli | Launch the scheduler ⏲️
twitter_makeup_cli | Every 1 day at 07:30:00 do change_display_name(name='Nicolas Dupont ☕') (last run: [never], next run: 2020-05-03 07:30:00)
twitter_makeup_cli | Every 1 day at 08:30:00 do change_display_name(name='Nicolas Dupont 💻') (last run: [never], next run: 2020-05-03 08:30:00)
twitter_makeup_cli | Every 1 day at 13:39:00 do change_display_name(name='Nicolas Dupont ☕') (last run: [never], next run: 2020-05-03 13:39:00)
twitter_makeup_cli | Every 1 day at 06:30:00 do change_banner_picture(path='config/images/banner-night.jpg') (last run: [never], next run: 2020-05-03 06:30:00)
twitter_makeup_cli | Every 1 day at 21:00:00 do change_banner_picture(path='config/images/banner-morning.jpg') (last run: [never], next run: 2020-05-02 21:00:00)
twitter_makeup_cli | Every 1 week at 18:30:00 do change_profile_picture(path='config/images/profile-weekend.jpg') (last run: [never], next run: 2020-05-08 18:30:00)
twitter_makeup_cli | Every 1 week at 07:30:00 do change_profile_picture(path='config/images/profile-week.jpg') (last run: [never], next run: 2020-05-04 07:30:00)
twitter_makeup_cli | Current time = 14:04:47

twitter_makeup_cli | Profile name has been changed for "Nicolas Dupont ☕" 🦄
```

## Logs 📃

You can launch it as a dameon `docker-compose up -d`

The logs are stored into `log/makeup.log`

## Api Rate Limits ⚠️

Be cautious with the [Twitter API Rate Limits](https://developer.twitter.com/en/docs/basics/rate-limiting)

## License 🗏

[MIT License](LICENSE)

## Dependencies 📦

This tool uses:
  - [Tweepy](https://www.tweepy.org/), using only a (very) small subset of its capabilities.
  - [schedule](https://schedule.readthedocs.io/en/stable/), Python scheduling for humans.
