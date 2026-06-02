TOOLS = [
    {
        "name": "scrape_webpage",
        "description": """Uses Firecrawl API to scrape a singular webpage. A dictionary of the scraped page 
        contents in the format requested (e.g. html, markdown, etc...)..""",
        "input_schema": {
            "type": "object",
            "properties": {
                "usr_url": {
                    "type" : "str",
                    "description": "User URL of the wepage they would like to scrape the contents of."
                },
                "usr_formats": {
                    "type" : "Literal['markdown', 'html']",
                    "description": "Available formats for the scraped URL to be formatted into."
                }
            }
        },
        "required": ['usr_url', 'usr_formats']
    },
    {
        "name" : "crawl_webpage",
        "description": """Uses Firecrawl API to crawl an initital webpage URL and then scrape all other URL's 
        found in the initial webpage and outputs their contents in a dictionary.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "usr_url": {
                    "type" : "str",
                    "description" : "Initial webpage URL that the user requests to be crawled."
                },
                "usr_lim": {
                    "type" : "int",
                    "description" : "User designated limit on how many webpages the Firecrawl API will crawl before stopping."
                },
                "usr_scrape_option": {
                    "type": """
                    class CrawlDict(TypedDict):
    
                        '''
                        ## Args
                        
                        1. formats (REQUIRED): Dictates what format the content should be returned in.
                        2. onlyMainContent (OPT.): Strips out navbars, footers, ads, and only returns 
                        the body content of the webpage.
                        3. includeTags (OPT.): Tags that will be included in the scrape result.
                        4. excludeTags (OPT.): Tags that will be excluded in the scrape result.
                        5. waitFor (OPT.): The amount of milliseconds to wait before scraping (useful 
                        for JS-heavy pages)
                        6. screenshot (OPT.): Captures a screenshot of each webpage.
                        '''
                        
                        formats: Literal['markdown', 'html']
                        onlyMainContent: NotRequired[Literal[True, False]]
                        includeTags: NotRequired[Literal['img', 'table']]
                        excludeTags: NotRequired[Literal['img', 'table']]
                        waitFor: NotRequired[int]
                        screenshot: NotRequired[Literal[True, False]]
                    """,
                    "description": "Custom class that dictates a custom dictionary with optional fields that controls the outcome of the page crawl."
                }
            },
        },
        "required": ['usr_url', 'usr_lim','usr_scrape_option']
    },
    {
        "name" : "search_webpage",
        "description" : """Uses Firecrawl API to search for given user query, to which Firecrawl will return a list of dictionaries of the most applicable 
        webpages related to the user query and their URL, title, description, and formatted contents in markdown.""",
        "input_schema": {
            "type": "object",
            "properties" : {
                "web_search" : {
                    "type" : "str",
                    "description" : "User inquiry in a form similar to a search placed into a search engine."
                }
            }
        },
        "required": ['web_search']
    }, 
    {
        "name" : "stop_react_loop",
        "description" : "Used when LLM deems a given problem as solved and needs no more use of tools to finish user problem.",
        "input_schema": {
            "type" : "object",
            "properties" : {}
        },
        "required" : []
    },
    {
        "name": "call_anthropic",
        "description": """Calls the Anthropic LLM when a user inquiry doesn't fall into the territory of webpage scraping or crawling, or 
        general inquiries in general.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "prompt" : {
                    "type": "str",
                    "description": "prompt given to the anthropic LLM thats used as the inference."
                },
                "chat_history" : {
                    "type" : "Notepad object | dict",
                    "description": """Is either a Notepad object that keeps track of the current chat history and tool uses, or 
                    just a regular dict of the the LLM/user chat history."""
                },
                "is_reacting" : {
                    "type" : "bool",
                    "description" : "Boolean that dictates whether or not the LLM call is part of a react loop sequence."
                },
                "model" : {
                    "type" : "Type[ResponseModel]",
                    "description" : "Structured output model that the LLM will output the response in."
                }
            }
        }
    }
]