import anthropic
import instructor

from settings import anthropic_api_key, tools
from models import (SummaryModel, ReasoningModel, ActionModel, ObservationModel,
                    SearchEngineModel, SynthesizerModel)
from notepad import Notepad
from prompts import REASONING_PROMPT, ACTION_PROMPT, OBSERVATION_PROMPT, SYNTHESIZER_PROMPT
from typing import TypeVar, Type
from fc_scraper import crawl_webpage, scrape_webpage, search_webpage
from utils import (handle_format_selection, handle_limit_selection,
                   handle_create_crawlDict)
from logger import get_logger

log = get_logger(__name__)

claude = instructor.from_anthropic(anthropic.Anthropic(api_key=anthropic_api_key))

ResponseModel = TypeVar('ResponseModel', SummaryModel, ReasoningModel, 
                        ActionModel, ObservationModel, SearchEngineModel)

def call_anthropic(
    prompt: str,
    chat_history: Notepad | dict,
    is_reacting: bool,
    model: Type[ResponseModel],
) -> ResponseModel:

    MODEL = "claude-sonnet-4-5" if not is_reacting else "claude-haiku-4-5"
    MAX_TOKENS = 4096 if not is_reacting else 1096

    curr_notepad = chat_history.get_notepad() if isinstance(chat_history, Notepad) else chat_history

    if not curr_notepad:
        pass

    if isinstance(chat_history, Notepad):
        chat_history.add({"role": "user", "content": prompt})
    else:
        chat_history.append({"role": "user", "content": prompt})

    log.debug("LLM call | model=%s max_tokens=%d response_model=%s", MODEL, MAX_TOKENS, model.__name__)

    response = claude.messages.create(
        model = MODEL,
        max_tokens = MAX_TOKENS,
        messages = chat_history,
        response_model = model
    )

    log.debug("LLM response | model=%s response_model=%s", MODEL, model.__name__)

    return response

def call_anthropic_react(usr_prompt: str, chat_history: Notepad) -> str:
    log.info("ReAct step started | turns_remaining=%d", chat_history.turns)

    # Reasoning
    reason = reasoning(usr_prompt=usr_prompt, chat_history=chat_history)
    log.info("Reasoning | %s", reason.reason)

    chat_history.add({
        "role": "assistant",
        "content": reason.reason
    })

    # Action
    llm_action = action(chat_history=chat_history, reasoning=reason.reason)
    log.info("Action selected | tool=%s", llm_action.action)

    chat_history.add({
        "role": "assistant",
        "content": llm_action.action
    })

    if llm_action.action == "stop_react_loop":
        return llm_action.action

    # Observation
    llm_observation = observatiton(tool_name=llm_action, chat_history=chat_history)
    log.info("Observation | %s", llm_observation.observation)

    chat_history.add({
        "role": "assistant",
        "content": llm_observation.observation
    })

    return llm_action.action

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

def observatiton(tool_name: ActionModel, chat_history: Notepad) -> ObservationModel:
    
    tool_result = handle_tool_execution(tool_name.action)
    
    chat_history.add(tool_result)
    
    observation_prompt = OBSERVATION_PROMPT.format(chat=chat_history.get_notepad())
    
    result = call_anthropic(
        prompt=observation_prompt,
        chat_history=chat_history.get_notepad(),
        is_reacting=True,
        model=ObservationModel
    )
    
    return result

def synthesize(chat_history: Notepad) -> SynthesizerModel:
    
    synthesizer_full_prompt = SYNTHESIZER_PROMPT.format(chat=chat_history.get_notepad())
    
    result = call_anthropic(
        prompt=synthesizer_full_prompt,
        chat_history=chat_history.get_notepad(),
        is_reacting=False,
        model=SynthesizerModel
    )
    
    return result

def handle_tool_execution(tool_name: str) -> dict:
    log.info("Executing tool | tool=%s", tool_name)

    if tool_name == "stop_react_loop":
        log.info("ReAct loop stopping")
        return {
            "tool_name" : "stop_react_loop"
        }

    elif tool_name == "scrape_webpage":
        url = input("Enter webpage URL to scrape: ")
        format = handle_format_selection()
        log.debug("scrape_webpage | url=%s format=%s", url, format)
        results = scrape_webpage(usr_url=url, usr_formats=format)
        log.info("scrape_webpage complete | url=%s", url)
        return results

    elif tool_name == "crawl_webpage":
        url = input("Enter webpage URL to scrape: ")
        limit = handle_limit_selection()
        crawler_config = handle_create_crawlDict()
        log.debug("crawl_webpage | url=%s limit=%d", url, limit)
        crawl_results = crawl_webpage(usr_url=url, usr_lim=limit, usr_scrape_options=crawler_config)
        log.info("crawl_webpage complete | url=%s", url)
        return crawl_results

    elif tool_name == "search_webpage":
        usr_search = input("What would you like to search for?: ")
        log.debug("search_webpage | query=%s", usr_search)

        SEARCH_PROMPT = f"""
        You are a professional at converting user inquiries into search engine statments.
        Below I am going to provide you with a search the user is making and I want you to
        convert it to an appropriate statement a user would type into a search engine.

        <inquiry>
            {usr_search}
        </inquiry>
        """

        chat = [{
            "role": "user",
            "content": SEARCH_PROMPT
        }]

        search = call_anthropic(prompt=SEARCH_PROMPT, chat_history=chat,
                       is_reacting=False, model=SearchEngineModel)
        log.info("search_webpage complete | query=%s", usr_search)
        return search