from pydantic import Field, BaseModel
from typing import TypedDict, NotRequired, Literal

class SummaryModel(BaseModel):
    
    summary: str = Field(description="Easy to read, user-friendly summary of the LLM response to be shown to the user.")
    
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
    