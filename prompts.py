FIRECRAWL_AGENT_INIT_PROMPT="""

"""

REASONING_PROMPT="""
You are an expert at reasoning and breaking down a problem step by step. I am going to provide you 
with a prompt/inquiry alongside all available tools and I want you to reason on how to solve the inquiry.

<inquiry>
    {inquiry}
</inquiry>

<tools>
    {tools}
</tools>
"""

ACTION_PROMPT="""
You are an expert at selecting appropriate tools to solve a problem. I am going to provide you with a reasoning flow 
regarding a user problem and I want you to select the next appropriate tool to be called to solve the current 
piece of the problem at hand.

<reasoning>
    {reasoning}
</reasoning>

<tools>
    {tools}
</tools>
"""

OBSERVATION_PROMPT="""
You are an expert at making observations given a chat history between a user and an LLM. I am going to provide you with 
the current chat history (where the last thing to hapen was a tool executing) and I want you to make an observation of 
the current chat.

<chat>
    {chat}
</chat>
"""
