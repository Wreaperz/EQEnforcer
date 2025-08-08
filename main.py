from reddit_client import stream_new_posts
from openai_client import moderate_post
from decision_engine import parse_verdict
from actions import warn_user, remove_post, log_action

# Uncomment this to test in a different subreddit
#SUBREDDIT_OVERRIDE = "legitEQ_Test"
SUBREDDIT_OVERRIDE = None  # Use config.default


def handle_submission(submission):
    flair = submission.link_flair_text or ""
    title = submission.title or ""

    print(f"Testing post: {title}")
    body = submission.selftext or ""
    
    response = moderate_post(title, body)
    print("Raw LLM response:", response)

    verdict, reason = parse_verdict(response)
    print(f"Verdict: {verdict} | Reason: {reason}")

    if verdict == "warn":
        warn_user(submission, reason)
        log_action(submission.id, "warn", reason)

    elif verdict == "remove":
        remove_post(submission, reason)
        log_action(submission.id, "remove", reason)

    else:
        log_action(submission.id, "approve", reason)


if __name__ == "__main__":
    import praw

    reddit = praw.Reddit("eqenforcer")
    print(f"Logged in as: {reddit.user.me()}")
    
    for submission in stream_new_posts(SUBREDDIT_OVERRIDE):
        handle_submission(submission)

