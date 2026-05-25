from typing import List, Optional

from pydantic import BaseModel, Field, model_validator
from datetime import datetime, timezone

class CreateDocument(BaseModel): 
    document_name: str = Field(..., max_length=255)
    file_path: str = Field(..., max_length=255)


class UpdateDocument(BaseModel): 
    document_name: Optional[str] = Field(min_length=1, max_length=255)

class ReadDocument(BaseModel): 
    id: int
    documnet_name: str
    file_path: str
    status: str 
    created_at: datetime = Field(default_facory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @model_validator(mode="before")
    def convert_status_to_str(cls, values): 
        status = values.get("status")
        if status is not None: 
            values["status"] = status.name
        return values
    
class ListDocuments(BaseModel): 
    documents: List[ReadDocument]

    