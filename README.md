# EQEnforcer

**Python LLM-based Reddit moderator** that monitors r/legitEQ for off-topic or near–off-topic posts, then removes or comments on them automatically.

---

## Features

- Connects to Reddit via PRAW using credentials from `praw.ini`
- Reads your OpenAI API key from `.env`
- Analyzes posts with OpenAI LLM to decide whether they’re off-topic
- Either removes or flags posts accordingly  

---

## Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/Wreaperz/EQEnforcer.git
   cd EQEnforcer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure `.env`:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Configure `praw.ini` with your Reddit credentials:
   ```ini
   [eqenforcer]
   client_id=YOUR_CLIENT_ID
   client_secret=YOUR_CLIENT_SECRET
   username=EQEnforcer
   password=YOUR_REDDIT_PASSWORD
   user_agent=eq-mod-bot/0.1 by u/EQEnforcer
   ```

---

## Usage

Run the bot:
```bash
python main.py
```

What happens:
- Streams or fetches posts from r/legitEQ
- Uses `openai_client.py` to send LLM prompts
- Decision logic in `decision_engine.py` decides remove vs. comment
- Actions happen via `actions.py`, using Reddit client (`reddit_client.py`)

---

## File Structure

```
.
├── .env                # OpenAI API key
├── praw.ini            # Reddit credentials
├── main.py             # Entry point
├── openai_client.py    # OpenAI integration
├── reddit_client.py    # Reddit API handling
├── decision_engine.py  # Topic analysis logic
├── actions.py          # Removal/comment logic
├── config.py           # Config and parameter setup
├── prompts/            # LLM prompt templates
└── requirements.txt    # Python dependencies
```

---

## Configuration & Tuning

- Adjust prompt templates inside `prompts/`
- Tweak thresholds or logic in `decision_engine.py`
- Logging or notification features can be added via `config.py`

---

## License

This project is licensed under the [MIT License](LICENSE).
