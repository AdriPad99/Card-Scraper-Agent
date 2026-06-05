from fc_agent import call_anthropic_react, synthesize
from notepad import Notepad

notepad = Notepad(turns=0)
chat_history = []

def main():
    
    print(
        "\n=== Web Research Agent ===\n"
        "I can help you with:\n"
        "  - Scraping a webpage       (e.g. 'scrape https://example.com')\n"
        "  - Crawling a website       (e.g. 'crawl https://docs.example.com up to 10 pages')\n"
        "  - Searching the web        (e.g. 'search for the latest AI news')\n"
        "  - General questions        (e.g. 'summarize what you found')\n"
    )
    prompt = input("What would you like to research? > ")
    
    while True:
        
        if notepad.get_turn_count() >= 10:
            
            break
        
        react_loop_result = call_anthropic_react(prompt, notepad)
        
        notepad.increase_turn_count()
        
        if react_loop_result == "stop_react_loop":
            
            result = synthesize(notepad)
            
            print(result.summary)
            
            break
        


if __name__ == "__main__":
    main()
