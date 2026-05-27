from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class JobCreate(BaseModel): 
    document_id: Int

class JobRead(BaseModel): 
    id: int
    document_id: int = Field()
    status: str
    attempt_count: int = Field(default=0)
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    failed_at: Optional[datetime]

class JobUpdate(BaseModel): 
    status: Optional[str]
    attempt_count: Optional[int]
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    failed_at: Optional[datetime]