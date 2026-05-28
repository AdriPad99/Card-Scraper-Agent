import anthropic
import instructor

from settings import anthropic_api_key
from models import SummaryModel, ReasoningModel, ActionModel, ObservationModel
from notepad import Notepad
from prompts import REASONING_PROMPT, ACTION_PROMPT, OBSERVATION_PROMPT

claude = instructor.from_anthropic(anthropic.Anthropic(api_key=anthropic_api_key))

MODEL = "claude-sonnet-4-5"
MAX_TOKENS = 4096

def call_anthropic(prompt: str, chat_history: list[dict]) -> SummaryModel:
    
    """Prompts claude with given user input and ouputs LLM response in the form of a 
    SummaryModel structured pydantic object.
    
    ## Args
    
        1. prompt: User input gathered from user to be sent to LLM
        2. chat_history: Current chat history for the LLM to reference
    """
    
    if not chat_history:
        
        pass
    
    chat_history.append({
        "role": "user",
        "content": prompt
    })
    
    response = claude.messages.create(
        model = MODEL,
        max_tokens = MAX_TOKENS,
        messages = chat_history,
        response_model = SummaryModel
    )
    
    return response

def call_anthropic_react(usr_prompt: str):
    
    # Reasoning
    
    
    # Action
    
    
    # Observation
    
    
    pass

def reasoning(usr_prompt: str) -> ReasoningModel:
    
    
    
    pass

def action() -> ActionModel:
    
    pass

def observatiton() -> ObservationModel:
    
    pass