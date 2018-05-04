import tweepy
import requests
from secrets import *
from time import sleep

#OAuthHandler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

 # API instance
api = tweepy.API(auth)

#Creating a user class
class Individual:
    def __init__(self, name):
        mostrecenttweet = api.user_timeline(name)[0]
        self.mostrecenttweet = mostrecenttweet.text
        self.id = mostrecenttweet.id
        self.name = name
        self.lasttweet = ''

    def modify_last(self,last):
        self.lasttweet = last

    def modify_recent(self,recent):
        self.mostrecenttweet = recent

    def modify_id(self, stat_id):
        self.id = stat_id

def classCreation(list):
    people = []
    for person in list:
        user = Individual(person)
        people.append(user)

    return people

def runTime(follow):

    while True:
        try:

            for follower in follow:

                print('Last Tweet: '+ follower.lasttweet)
                print('Most Recent Tweet: '+follower.mostrecenttweet)


                if follower.mostrecenttweet != follower.lasttweet:
                    api.retweet(follower.id)
                    line = "Something"
                    print(line)

                # updates lasttweet to the most recent tweet
                follower.modify_last(follower.mostrecenttweet)

                #fetching the most recent tweet again
                update = api.user_timeline(follower.name)[0]
                follower.modify_recent(update.text)
                follower.modify_id(update.id)
                sleep(2)

        except tweepy.TweepError as e:
            print(e.message)


        print("sleeping")
        print('\n')
        sleep(60 * 5)  # Sleep for 5 seconds

following = ['VRustomji','theyashbhardwaj']
individuals = classCreation(following)
runTime(individuals)