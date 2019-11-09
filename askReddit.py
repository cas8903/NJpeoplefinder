import praw
#go to preferences, project interpreter and search 'praw' to install to pycharm


#TODO
#creates an instance of reddit
reddit=praw.reddit(args)
#enable read only mode
reddit.read_only=True

#TODO define reddit instance
askReddit = reddit.subreddit('AskReddit')
#TODO read all submissions into a database
#TODO read all comments into a relational database
#use MONGO DB?



