from pydantic import BaseModel, Field
from logger import get_logger

log = get_logger(__name__)

class Notepad(BaseModel):

    turns: int = 10
    notepad: list = Field(default_factory=list)

    def add(self, item: dict):
        role = item.get("role", "unknown")
        log.debug("Notepad.add | role=%s len_after=%d", role, len(self.notepad) + 1)
        self.notepad.append(item)

    def clear(self):
        log.debug("Notepad.clear | cleared %d entries", len(self.notepad))
        self.notepad = []

    def get_notepad(self):
        return self.notepad

    def increase_turn_count(self):
        self.turns += 1
        log.debug("Notepad.turns -> %d", self.turns)

    def decrement_turn_count(self):
        self.turns -= 1
        log.debug("Notepad.turns -> %d", self.turns)

    def set_turn_count(self, count: int):
        log.debug("Notepad.set_turn_count | %d -> %d", self.turns, count)
        self.turns = count
        
    def get_turn_count(self):
        
        return self.turns