import os
from typing import Optional

import tweepy

# NOTE: We are **not** using the google.adk.tools @tool decorator to avoid
# introducing a hard dependency on the ADK runtime inside this utility module.
# The function can still be registered as a tool by passing the callable to a
# google.adk.Agent.

def post_to_x(content: str, *, reply_to_tweet_id: Optional[str] = None) -> str:
    """Post a text update to X (Twitter).

    For an MVP we only support posting *plain text* tweets. Media uploads,
    threads, and polls can be added later following the X API documentation.

    Environment variables expected (populate them in `.env`):
    * ``X_BEARER_TOKEN``
    * ``X_API_KEY``
    * ``X_API_SECRET``
    * ``X_ACCESS_TOKEN``
    * ``X_ACCESS_TOKEN_SECRET``

    Args:
        content: The text to be posted. If it exceeds 280 characters, it will
            be truncated and an ellipsis will be appended.
        reply_to_tweet_id: (optional) If supplied the new post will be a reply
            to the given tweet.

    Returns:
        The URL of the created post or a descriptive error message.
    """
    # Ensure we do not exceed the hard-limit of 280 characters.
    if len(content) > 280:
        content = content[:277] + "..."

    api_key = os.getenv("X_API_KEY")
    api_secret = os.getenv("X_API_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_secret = os.getenv("X_ACCESS_TOKEN_SECRET")
    bearer_token = os.getenv("X_BEARER_TOKEN")

    missing = [name for name, value in {
        "X_API_KEY": api_key,
        "X_API_SECRET": api_secret,
        "X_ACCESS_TOKEN": access_token,
        "X_ACCESS_TOKEN_SECRET": access_secret,
        "X_BEARER_TOKEN": bearer_token,
    }.items() if not value]

    if missing:
        return (
            "Error posting to X – missing environment variables: "
            + ", ".join(missing)
        )

    try:
        client = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_secret,
            wait_on_rate_limit=True,
        )

        response = client.create_tweet(
            text=content,
            in_reply_to_tweet_id=reply_to_tweet_id if reply_to_tweet_id else None,
        )
        tweet_id = response.data["id"]
        return f"https://twitter.com/i/web/status/{tweet_id}"

    except Exception as exc:  # pylint: disable=broad-except
        # Returning the error instead of raising keeps the agent workflow alive.
        return f"Error posting to X – {exc}" 