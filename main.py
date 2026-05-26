from fc_agent import call_anthropic
from fc_scraper import scrape_webpage

def main():
    
    test = call_anthropic()
    
    test2 = scrape_webpage()
    
    print("Hello from card-agent!")


if __name__ == "__main__":
    main()
