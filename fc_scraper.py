from settings import fc_api_key
from firecrawl import FirecrawlApp
from typing import Literal
from models import CrawlDict

app = FirecrawlApp(api_key=fc_api_key)

def scrape_webpage(usr_url: str, usr_formats: Literal["markdown", "html"]) -> dict:
    
    """
    Uses Firecrawl API to scrape a singular webpage. The contents of the webpage is 
    then returned in the requested format.
    
    ## Args
    
    1. usr_url: URL of the webpage the user/LLM would like to scrape and get the 
    results of.
    
    2. usr_formats: Format(s) of how the webpage contents should be scraped into.
    """
    
    data = app.scrape_url(url=usr_url, formats=usr_formats)
    
    return data

def crawl_webpage(usr_url: str, usr_lim: int, usr_scrape_options: CrawlDict) -> dict:
    
    """
    Uses Firecrawl API to crawl an initital webpage URL and then scrape all other URL's 
    found in the initial webpage and outputs their contents.
    
    ## Args
    
    1. usr_url: Initial URL that will be scraped
    
    2. usr_lim: Limit on how many crawls deep Firecrawl will search from the initial webpage.
    
    3. usr_scrape_options: Tells Firecrawl hot to scrape each individual page it discovers 
    during the crawl. This is dictated through a 'CrawlDict' passed into the argument with 
    custom parameters.
    """
    
    crawl_results = app.crawl_url(url=usr_url, limit=usr_lim, scrape_options=usr_scrape_options)
    
    return crawl_results