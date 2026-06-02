from fc_agent import call_anthropic_react, synthesize
from notepad import Notepad

notepad = Notepad(turns=0)
chat_history = []

def main():
    
    prompt = input("Hello, what can I help you with?: ")
    
    while True:
        
        if notepad.get_turn_count() >= 10:
            
            break
        
        react_loop_result = call_anthropic_react(prompt, notepad)
        
        notepad.increase_turn_count()
        
        if react_loop_result == "stop_react_loop":
            
            break
        
    result = synthesize(notepad)
    
    print(result.summary)


if __name__ == "__main__":
    main()
