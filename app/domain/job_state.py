from enum import Enum, auto
from dataclasses import dataclass, field

from app.domain.document_state import DocumentEvent, DocumentState
from app.domain.sm import StateMachine

class JobState(Enum): 
    PENDING = auto()
    PROCESSING = auto() 
    COMPLETED = auto()
    FAILED = auto()


class JobEvent(Enum): 
    CLAIM = auto()
    COMPLETE = auto()
    FAIL = auto()
    RETRY = auto()
    CANCEL = auto()

@dataclass
class JobCtx: 
    job_id: int
    document_id: int
    worker_id: int | None = None
    error_message: str | None = None
    audit: list[str] = field(default_factory = list)



document_state: StateMachine[JobState, JobEvent, JobCtx] = StateMachine()

@document_state.transition(JobState.PENDING, JobEvent.CLAIM, JobState.PROCESSING)
def begin_processing(ctx: JobCtx) -> None:
    ctx.audit.append(f"{ctx.job_id}: processing")

@document_state.transition(JobState.PROCESSING, JobEvent.COMPLETE, JobState.COMPLETED)
def completed_processing(ctx: JobCtx) -> None: 
    ctx.audit.append(f"{ctx.job_id}: completed")

@document_state.transition(JobState.PROCESSING, JobEvent.FAIL, JobState.FAILED)
def failed_processing(ctx: JobCtx) -> None: 
    ctx.audit.append(f"{ctx.job_id}: failed")

@document_state.transition(
    (
        JobState.PENDING,
        JobState.PROCESSING,
        JobState.COMPLETED,
        JobState.FAILED,
    ),
    JobEvent.CANCEL,
    JobState.FAILED,
)

@dataclass
class Job: 
    ctx: JobCtx
    state: JobState = JobState.PENDING

    def handle(self, event: JobEvent): 
        self.state = document_state.handle(self.ctx, self.state, event)

  
