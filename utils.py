from typing import Literal
from models import CrawlDict
from logger import get_logger

log = get_logger(__name__)

def handle_format_selection() -> str:
    
    """
    Prompts the user for the format they would like the scrape be output in.
    """
    
    formats = ["markdown", "html"]
        
    format = input("What format would you like the content to be returned in? (markdown, html)")
        
    while True:
        
        if format not in formats:
            
            format = input("Please select an appropriate format (markdown, html)")
            
        else:
            
            break
            
    log.debug("Format selected | format=%s", format)
    return format

def handle_limit_selection() -> int:
    
    """
    Prompts the user for the amount of scrapes they want the Firecrawl API to make.
    """
    
    limit = input("How many crawls deep would you like (lim 50)")
        
    while True:
    
        try:
            
            usr_lim = int(limit)
            
            break
            
        except ValueError:
            
            print("Please enter an appropriate number")
            
    log.debug("Crawl limit selected | limit=%d", usr_lim)
    return usr_lim

def handle_main_content_selection() -> bool:
    
    """
    Handles prompting the user if they would like to remove any unnecesary information 
    from the webpage scrape.
    """
    
    usr_ans = input("Would you like to stip out the navbars, footers, and ads? (y/n)")
    
    responses = ['y', 'n']
    
    while True:
        
        if usr_ans not in responses:
            
            usr_ans = input("please enter an appropriate respoonse (y/n)")
            
        else:
            
            break
      
    usr_ans = usr_ans.lower()
        
    if usr_ans == 'y':
        
        return True
    
    elif usr_ans == 'n':
        
        return False
    
def handle_tags(type: Literal['include', 'exclude']) -> list:
    
    f"""
    Handles which tags the user would like to {type} in the scrape.
    """
    
    tag_selection = ['img', 'table', 'both', 'neither']
    
    included_tags = []
    
    tags = input(f"What tags would you like to {type}? (img, table, both, neither)")
    
    tags = tags.lower()
    
    while True:
        
        if tags not in tag_selection:
            
            tags = input("Please enter an appropriate option (img, table, both, neither)")
            
        else:
            
            break
        
    if tags == 'img':
        
        included_tags.append('img')
        
    elif tags == 'table':
        
        included_tags.append('table')
        
    elif tags == 'both':
        
        included_tags.append('img')
        included_tags.append('table')
        
    elif tags == 'neither':
        
        included_tags.append('neither')
        
    return included_tags

def handle_wait_time() -> int:
    
    """Handles letting the user to set the amount of time between scrapes."""
    
    usr_secs = input("How many seconds would you like to wait between scrapes? (lim. 30)")
    
    while True:
        
        try:
            
            usr_secs = int(usr_secs)
        
        except ValueError:
            
            usr_secs = input("Please enter an appropriate amount of seconds (lim. 30)")
            
        if usr_secs < 0 or usr_secs > 30:
            
            usr_secs = input("Please enter an appropriate amount of seconds (lim. 30)")
            
            continue
            
        else:
            
            break
        
    return usr_secs * 1000

def handle_enable_screenshot() -> bool:
    
    """
    Handles user decision if they want to enable screenshots
    """
    
    screenshot_enabled = input("Would you like a screenshot of every webpage scrape? (y/n)").lower()
    
    choices = ['y','n']
    
    while True:
        
        if screenshot_enabled not in choices:
    
            screenshot_enabled = input("Please select an appropriate option (y/n)").lower()
            
        else:
            
            break
        
    if screenshot_enabled == 'y':
        
        return True
    
    elif screenshot_enabled == 'n':
        
        return False
    
def handle_create_crawlDict() -> CrawlDict:
    
    """
    Handles the user creating the config for the web scrape
    """
    
    format = handle_format_selection()
        
    main_content_enabled = handle_main_content_selection()
    
    included_tags = handle_tags('include')
    
    excluded_tags = handle_tags('exclude')
    
    wait_time = handle_wait_time()
    
    screenshots_enabled = handle_enable_screenshot()
    
    return CrawlDict(
        formats=format,
        onlyMainContent=main_content_enabled,
        includeTags=included_tags,
        excludeTags=excluded_tags,
        waitFor=wait_time,
        screenshot=screenshots_enabled
    )