import os
from dotenv import load_dotenv

load_dotenv()

SUBREDDIT_NAME = "legitEQ"
PRAW_CONFIG = "eqenforcer"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o"

BOT_USERNAME = "EQEnforcer"  # exact Reddit username of the bot
MENTION_TRIGGERS = [f"u/{BOT_USERNAME.lower()}", f"/u/{BOT_USERNAME.lower()}", BOT_USERNAME.lower()]
MENTION_REPLY_COOLDOWN_MIN = 10  # basic safety if you want, not critical
USE_LLM_FOR_MENTION_REPLY = True  # set True to craft tailored replies with OpenAI
