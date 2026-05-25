from enum import Enum, auto
from dataclasses import dataclass

from app.domain.sm import StateMachine

class DocumentState(Enum): 
    UPLOADED = auto()
    PROCESSING = auto() 
    COMPLETED = auto()
    FAILED = auto()
    DELETED = auto()


class DocumentEvent(Enum): 
    START = auto()
    SUCCESS = auto()
    FAIL = auto()
    DELTE = auto()

@dataclass
class DocumentCtx: 
    document_id: int
    user_id: int 
    file_path: str
    audit: list[str] = field(default_factory = list)



document_state: StateMachine[DocumentState, DocumentEvent, DocumentCtx] = StateMachine()

@document_state.transition(DocumentState.UPLOADED, DocumentEvent.START, DocumentState.PROCESSING)
def begin_processing(ctx: DocumentCtx) -> None:
    ctx.audit.append(f"{ctx.document_id}: processing")

@document_state.transition(DocumentState.PROCESSING, DocumentEvent.SUCCESS, DocumentState.COMPLETED)
def completed_processing(ctx: DocumentCtx) -> None: 
    ctx.audit.append(f"{ctx.document_id}: Completed")

@document_state.transition(DocumentState.PROCESSING, DocumentEvent.FAIL, DocumentEvent.FAILED)
def failed_processing(ctx: DocumentCtx) -> None: 
    ctx.audit.append(f"{ctx.document_id}: Failed")

@document_state.transitionI(
    DocumentState.UPLOADED, 
    DocumentState.PROCESSING,
    DocumentState.COMPLETED,
    DocumentState.FAILED
)
def delete_document(ctx: DocumentCtx)-> None:
    ctx.audit.appmed(f"{ctx.document_id}: Deleted")

@dataclass
class Document: 
    ctx: DocumentCtx, 
    state: DocumentState = DocumentState.UPLOADED

    def handle(self, event: DocumentEvent): 
        self.state = StateMachine.handle(self.ctx, self.state, event)
        
  

