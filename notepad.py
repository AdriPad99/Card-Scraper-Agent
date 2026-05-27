from pydantic import BaseModel, Field

class Notepad(BaseModel):
    
    turns: int = 10
    notepad = Field(default_factory=list)
    
    def add(self, item: str):
        
        self.notepad.append(item)
        
    def clear(self):
        
        self.notepad = []
        
    def increase_turn_count(self):
        
        self.turns += 1
        
    def decrement_turn_count(self):
        
        self.turns -= 1
        
    def set_turn_count(self, count: int):
        
        self.turns = count