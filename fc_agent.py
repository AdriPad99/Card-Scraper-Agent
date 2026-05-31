import anthropic
import instructor

from settings import anthropic_api_key, tools
from models import SummaryModel, ReasoningModel, ActionModel, ObservationModel
from notepad import Notepad
from prompts import REASONING_PROMPT, ACTION_PROMPT, OBSERVATION_PROMPT
from typing import TypeVar, Type
from fc_scraper import crawl_webpage, scrape_webpage, search_webpage

claude = instructor.from_anthropic(anthropic.Anthropic(api_key=anthropic_api_key))

ResponseModel = TypeVar('ResponseModel', SummaryModel, ReasoningModel, ActionModel, ObservationModel)

def call_anthropic(
    prompt: str,
    chat_history: Notepad,
    is_reacting: bool,
    model: Type[ResponseModel],
) -> ResponseModel:
    
    MODEL = "claude-sonnet-4-5" if not is_reacting else "claude-haiku-4-5"
    MAX_TOKENS = 4096 if not is_reacting else 1096
    
    """Prompts claude with given user input and ouputs LLM response in the form of a 
    SummaryModel structured pydantic object.
    
    ## Args
    
        1. prompt: User input gathered from user to be sent to LLM
        2. chat_history: Current chat history for the LLM to reference
    """
    
    curr_notepad = chat_history.get_notepad()
    
    if not curr_notepad:
        
        pass
    
    chat_history.add({
        "role": "user",
        "content": prompt
    })
    
    response = claude.messages.create(
        model = MODEL,
        max_tokens = MAX_TOKENS,
        messages = chat_history,
        response_model = model
    )
    
    return response

def call_anthropic_react(usr_prompt: str, chat_history: Notepad):
    
    # Reasoning
    
    
    # Action
    
    
    # Observation
    
    
    pass

def reasoning(usr_prompt: str, chat_history: Notepad) -> ReasoningModel:
    
    reasoning_prompt = REASONING_PROMPT.format(inquiry=usr_prompt, tools=tools)
    
    result = call_anthropic(prompt=reasoning_prompt, 
                   chat_history=chat_history.get_notepad(),
                   is_reacting=True,
                   model=ReasoningModel)
    
    return result

def action(chat_history: Notepad, reasoning: str) -> ActionModel:
    
    action_prompt = ACTION_PROMPT.format(reasoning=reasoning, tools=tools)
    
    result = call_anthropic(prompt=action_prompt,
                            chat_history=chat_history.get_notepad(),
                            is_reacting=True,
                            model=ActionModel)
    
    return result

def observatiton(usr_prompt: str, chat_history: Notepad) -> ObservationModel:
    
    
    
    pass

def handle_tool_execution(tool_name: str) -> dict:
    
    if tool_name == "stop_react_loop":
        
        return {
            "tool_name" : "stop_react_loop"
        }
        
    elif tool_name ==  "scrape_webpage":
        
        url = input("Enter webpage URL to scrape: ")
        
        choices = ["1", "2"]
        
        web_format = input("What format should it be parsed into? (1. markdown, 2. html)")
        
        while web_format not in choices:
            
            web_format = input("Please select an appropriate option (1. markdown, 2. html)")
            
        choice = ""
            
        if web_format == "1":
            
            choice = "markdown"
            
        elif web_format == "2":
            
            choice = "html"
            
        results = scrape_webpage(usr_url=url, usr_formats=choice)
        
        return results
    
    elif tool_name == "crawl_webpage":
        
        pass