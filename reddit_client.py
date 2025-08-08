import praw
from config import PRAW_CONFIG, SUBREDDIT_NAME as DEFAULT_SUBREDDIT_NAME

def get_reddit_instance():
    return praw.Reddit(PRAW_CONFIG)

def stream_new_posts(subreddit_override=None):
    reddit = get_reddit_instance()
    subreddit_name = subreddit_override or DEFAULT_SUBREDDIT_NAME
    print(f"Listening to new posts in r/{subreddit_name}...")
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.stream.submissions(skip_existing=True):
        yield submission
