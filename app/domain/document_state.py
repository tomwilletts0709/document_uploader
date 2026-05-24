from enum import Enum, auto
from dataclasses import dataclass

from app.domain.sm import StateMachine

class DocumentState(Enum): 
    UPLOADED = auto()
    PROCESSESING = auto() 
    COMPLETED = auto()
    FAILED = auto()
    DELETED = auto()


class DocumentEvent(Enum): 
    START = auto()
    SUCCESS = auto()
    FAIL = auto()

@dataclass
class DocumentCtx: 
    document_id: int
    user_id: int 
    file_path: str



document_state: StateMachine[DocumentState, DocumentEvent, DocumentCtx] = StateMachine()

@document_state.transition()
