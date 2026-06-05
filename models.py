from pydantic import Field, BaseModel
from typing import TypedDict, NotRequired, Literal

class SummaryModel(BaseModel):
    
    summary: str = Field(description="Easy to read, user-friendly summary of the LLM response to be shown to the user.")
    
class ReasoningModel(BaseModel):
    
    """Returns 'reason'"""
    
    reason: str = Field(description="Summary of the LLM's internal reasoning of a certain step.")
    
class ActionModel(BaseModel):
    
    """Returns 'action'"""
    
    action: Literal['scrape_webpage', 'crawl_webpage', 'search_webpage', 'stop_react_loop', 'handle_get_user_input'] = Field(description="Tool that LLM selects to solve the next step of the current problem.")
    
class ObservationModel(BaseModel):
    
    """Returns 'observation'"""
    
    observation: str = Field(description="Easy to read observation of the current LLM chat history and the results of tool calls.")
    
class SynthesizerModel(BaseModel):
    
    """Returns 'summary'"""
    
    summary: str = Field(description="User friendly, easy to read summary of the LLM chat and tool calls.")
    
class SearchEngineModel(BaseModel):
    
    """Returns 'search'"""
    
    search: str = Field(description="An equivalent search engine inquiry that matches with the user input.")
    
class CrawlDict(TypedDict):
    
    """
    Dict used only for crawling a webpage.
    
    ## Args
    
    1. formats (REQUIRED): Dictates what format the content should be returned in.
    2. onlyMainContent (OPT.): Strips out navbars, footers, ads, and only returns 
    the body content of the webpage.
    3. includeTags (OPT.): Tags that will be included in the scrape result.
    4. excludeTags (OPT.): Tags that will be excluded in the scrape result.
    5. waitFor (OPT.): The amount of milliseconds to wait before scraping (useful 
    for JS-heavy pages)
    6. screenshot (OPT.): Captures a screenshot of each webpage.
    """
    
    formats: Literal['markdown', 'html']
    onlyMainContent: NotRequired[Literal[True, False]]
    includeTags: NotRequired[Literal['img', 'table']]
    excludeTags: NotRequired[Literal['img', 'table']]
    waitFor: NotRequired[int]
    screenshot: NotRequired[Literal[True, False]]
    