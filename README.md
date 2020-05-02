# Make up your Twitter Profile! [docker service]

Small service to automate the make up of your twitter profile, from 🐴 to 🦄 !

Based on a crontab and Twitter API, you can change your profile at any day 📅 or any hour 🕒.

You can see it live on my [Twitter profile](https://twitter.com/duponico) 🐦

## Examples 🦄

Examples                                    | Result
------------------------------------------- | ------------------------------
Change the banner for the day               | ![alt text](./config/images/banner-morning.jpg "Morning banner")
And the night                               | ![alt text](./config/images/banner-night.jpg "Night banner")
Change your display name the morning        | Nico ☕
And during the day                          | Nico 💻
And for the night                           | Nico 😴
Change your profile picture for xmas        | ![alt text](./config/images/profile-xmas.jpg "XMas avatar")

You can also change your location when travelling, or description when you attend an event for instance.

## Install 🐋

Clone the repository:

```
git clone git@github.com:nidup/twitter-makeup-service.git
```

Build the Docker image:

```
docker-compose build
```

## Configure credentials 🔐

Twitter Make Up allows to programmatically change your profile on your behalf.

To configure it, you need to generate Twitter credentials.

[Follow the Twitter guide (OAuth 1.0a)](https://developer.twitter.com/en/docs/basics/authentication/overview).

Create a `secrets.py` file with your credentials in the `config` folder:

```
consumer_key = 'YourConsumerKey'
consumer_secret = 'YourConsumerSecret'
access_token = 'YourAccessToken'
access_secret = 'YourAccessSecret'
```

## Configure your Make Up Crontab 🐴 🦄









## Launch and Enjoy 

```
docker-compose up -d
```


## Publish the library

[Publish your library](https://medium.com/@thucnc/how-to-publish-your-own-python-package-to-pypi-4318868210f9)

Generate distribution archives

Make sure you have the latest versions of setuptools and wheel installed:
```
python3.6 -m pip install --user --upgrade setuptools wheel
```

Now run this command from the same directory where setup.py is located:
```
python3.6 setup.py sdist bdist_wheel
```

Uploading the distribution archives. To do this, you can use twine. First, install it using pip:
```
python3.6 -m pip install --user --upgrade twine
```

Then upload all the archives to PyPi:
```
python3.6 -m twine upload dist/*
```

Enter your PyPi username and password.

