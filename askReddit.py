""""""""""Chris Sequeira in conjunction with Connor Jackson
HackPrinceton2019"""""""""

#go to preferences, project interpreter and search 'praw' to install to pycharm
import praw
#use csv files for relational sumbissions->comments databases
import csv


#creates an instance of reddit
reddit=praw.reddit(user_agent='Sentiment analysis by Connor Jackson, Chris Sequeira')
#enable read only mode
reddit.read_only=True
#define reddit instance
askReddit = reddit.subreddit('AskReddit')

"""make a dictionary
keys = submissions
values = comments"""
posts = {}

#TODO narrow by time
#writes all submissions to a dictionary
for submission in askReddit.submissions.topAllTime():
    posts[submission]
    #writes each cubmission's comments
    #TODO fix
    for commentsCSV in submission:
        #add comments to new list every time
        #connect list to key
        posts[submission].add(comment)




