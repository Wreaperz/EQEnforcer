import datetime

def warn_user(submission, reason):
    msg = f"""
**Potential Issue Detected in Your Post**

The moderation bot flagged this post as potentially unproductive or inflammatory.

**Reason:** {reason}

No action has been taken yet. Please consider revising your post to better align with r/legitEQ's goals: thoughtful, emotionally intelligent discussion. If this was just a test post, no worries.
"""
    submission.reply(msg)


def remove_post(submission, reason):
    submission.mod.remove()
    submission.reply(f"""
**Post Removed Automatically**

**Reason:** {reason}

This post was flagged as not meeting the standards of r/legitEQ (emotionally intelligent, productive, non-inflammatory). If this removal was in error or this is a test, feel free to contact the mods.
""")


def log_action(post_id, action, reason):
    with open("logs/mod_log.txt", "a") as log:
        log.write(f"{datetime.datetime.now()} | {post_id} | {action.upper()} | {reason}\n")
