import os
from dotenv import load_dotenv

load_dotenv()

fc_api_key = os.getenv("FIRECRAWL_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")