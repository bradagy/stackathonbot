# This is a twitter bot that will tweet comedic financial advice
# to twitter users every 4 hours reminding them to stop spending money
# on unnecessary purchases and start saving.

import tweepy
import schedule
import time
import emoji
from time import sleep
from credentials import *
from datetime import *

# OAuth process, using the keys and the tokens. (Passing the keys into the function)
# The last line is to authenticate my account, once my keys are approved.
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Calculating the days until the Stackathon ends and updating
# the bot's tweet status.
today = date.today()
future = date(2019, 8, 18)
diff = future - today
message = 'The Stackathon ends in ' + str(diff.days) + \
    ' keep stacking' + ' \U0001F911' + '.'


def tweet_from_text_file():
    """Tweets a line from the StackathonBot text-file every four hours."""
    with open('StackathonBot.txt') as file:
        for line in file:
            if line != '\n':
                api.update_status(line)
                sleep(14400)
        else:
            pass


tweet_from_text_file()


def tweet_every_three_days():
    """Tweets the end of the Stackathon calculation message every 3 days."""
    schedule.every(72).hour.do(tweet_every_three_days())
    while True:
        schedule.run_pending()
        time.sleep(1)


tweet_every_three_days()