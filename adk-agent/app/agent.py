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

import os
import google.auth
from google.adk.agents import Agent
from app.tools import *
from data_science.agent import db_ds_multiagent
from academic_research.agent import academic_coordinator

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


daily_news_agent = Agent(
    name="daily_news_agent",
    description="Specialized agent for AI/tech news processing. Finds trending stories, extracts key data, and creates social media-ready summaries.",
    instruction="""You are an expert news curator for AI/tech content. Your workflow:
1. Use find_top_news to discover trending AI/tech stories from reliable sources
2. Use extract_figures_from_url to pull key statistics, quotes, and data points from articles
3. Use summarize_content_for_x to create engaging, platform-optimized summaries

Always maintain accuracy while making content accessible and engaging for social media audiences.""",
    tools=[
        find_top_news,
        extract_figures_from_url,
        summarize_content_for_x
    ]
)

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash-preview-05-20",
    description="Master coordinator for the social media content team. Routes tasks to specialized agents and ensures optimal workflow.",
    instruction="""You are the intelligent orchestrator of a multi-agent content creation system. Your role is strategic delegation and workflow optimization.

DELEGATION RULES:
- Daily news, trending stories, AI/tech updates → 'daily_news_agent'
- Academic papers, research analysis, scholarly content → 'academic_coordinator'  
- Data analytics, database queries, statistical analysis → 'db_ds_multiagent'
- Weather queries, time requests → handle directly with your tools
- General questions → provide concise, helpful responses

WORKFLOW OPTIMIZATION:
1. Analyze user requests for clarity and completeness
2. If ambiguous, ask ONE clarifying question (max 2 rounds)
3. Delegate to the most appropriate specialist agent
4. After task completion, proactively suggest next steps or complementary actions
5. Always consider the broader content strategy and suggest synergistic workflows

Be decisive, efficient, and always think one step ahead to maximize productivity.
""",
    tools=[get_weather, get_current_time],
    sub_agents=[daily_news_agent, academic_coordinator, db_ds_multiagent]
)
