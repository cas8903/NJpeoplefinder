"""Chris Sequeira
    Connor Jackson
    HackPrinceton 2019"""

import praw
import gcp


#creates an instance of reddit
reddit=praw.Reddit(user_agent='Sentiment analysis by Connor Jackson, Chris Sequeira', client_id='OPbpwRMkKTA1VA', client_secret="0CjJ_J3DrkyPUk3O2V2fE1dfJII", )
#enable read only mode
reddit.read_only=True

"""make a list format for values, submissions and comments"""
comments=[]

"""builds post from reddit link"""
def parseID(postid):
    submission = reddit.submission(id=postid)
    print("Title: ",submission.title)
    return submission

"""Writes comment body and post title to separate lists"""
def buildContent(submission):
    #strips noncomment interface components
    submission.comments.replace_more(limit=0)
    #writes each submission's comments
    for top_level_comment in submission.comments:
        #appends comments to the list of values
        comments.append(top_level_comment.body)
    return comments

"""Passes content to google for analysis"""
def gather_sentiment(comments):
    for comment in comments:
        gcp.gather_sentiment(comment)


def main():
    postid = input("Enter a reddit postID to evaluate sentiment: ")
    comments=buildContent(parseID(postid))
    gather_sentiment(comments)

    return 0

main()


