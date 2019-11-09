""""""""""Chris Sequeira in conjunction with Connor Jackson
HackPrinceton2019"""""""""

#go to preferences, project interpreter and search 'praw' to install to pycharm
import praw
import gcp


#creates an instance of reddit
reddit=praw.Reddit(user_agent='Sentiment analysis by Connor Jackson, Chris Sequeira', client_id='OPbpwRMkKTA1VA', client_secret="0CjJ_J3DrkyPUk3O2V2fE1dfJII", )
#enable read only mode
reddit.read_only=True
#define reddit instance
askReddit = reddit.subreddit('AskReddit')

#may be unnecessary
#__init__(site_name=None, requestor_class=None, requestor_kwargs=None, **config_settings)

"""make a dictionary
with a list format
for values
keys = submissions
values = comments"""
posts = {}
key=""
posts.setdefault(key, [])

#TODO narrow by time
#writes all submissions to a dictionary
for post in askReddit.submission.topAllTime():
    posts[post]
    #writes each cubmission's comments
    for top_level_comment in post.comments:
        #appends comments to the list of values
        posts[post].append(top_level_comment.body)

def gather_sentiment(posts):
    for i in posts.keys():
        for j in posts[i]:
            gcp.gather_sentiment(j)

def main():
    for content in posts.items():
        print(content)

    return 0


