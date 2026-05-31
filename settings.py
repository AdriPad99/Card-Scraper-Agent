import os
from dotenv import load_dotenv
from tools import TOOLS

load_dotenv()

fc_api_key = os.getenv("FIRECRAWL_API_KEY")
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

tools = ""

xml_tools_formatting = """<tool name='{tool_name}'>\n\t
                            <tool_description>\n\t\t
                                {tool_description}\n\t
                            </tool_description>\n
                           </tool>"""

for i in range(len(TOOLS)):
    
    curr_tool = xml_tools_formatting.format(tool_name=TOOLS[i]["name"], tool_description=TOOLS[i]["description"])
    
    tools += curr_tool