# tools.py
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
from zoneinfo import ZoneInfo

def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather.

    Args:
        query: A string containing the location to get weather information for.

    Returns:
        A string with the simulated weather information for the queried location.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        city: The name of the city to get the current time for.

    Returns:
        A string with the current time information.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for query {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


def find_top_news(query: str) -> str:
    """Finds the top news articles for a given query.

    Args:
        query: A string containing the topic to search for.

    Returns:
        A string with the top news articles for the queried topic.
    """
    return "The top news article URLs for the queried topic are: Google Achieved AGI, Meta's AI Agent is now available to all, and OpenAI's GPT-4 is the most powerful AI model yet."


def extract_figures_from_url(url: str) -> str:
    """Extracts the figures from a given URL.

    Args:
        url: A string containing the URL to extract figures from.

    Returns:
        A string with the figures from the URL.
    """
    return "The figures from the URL are: "


def summarize_content_for_x(content: str) -> str:
    """Summarizes the content for X.

    Args:
        content: A string containing the content to summarize.

    Returns:
        A string with the summarized content for X.
    """
    return "The summarized content for X is: "