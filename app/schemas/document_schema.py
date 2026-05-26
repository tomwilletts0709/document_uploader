from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator
from datetime import datetime, timezone


class DocumentCreate(BaseModel): 
    document_name: str = Field(..., max_length=255)
    file_path: str = Field(..., max_length=255)


class DocumentUpdate(BaseModel): 
    document_name: Optional[str] = Field(default=None, min_length=1, max_length=255)


class DocumentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    document_name: str
    file_path: str
    status: str 
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @model_validator(mode="before")
    def convert_status_to_str(cls, values): 
        if not isinstance(values, dict):
            values = {
                key: getattr(values, key)
                for key in cls.model_fields
                if hasattr(values, key)
            }

        status = values.get("status")
        if status is not None: 
            values["status"] = status.name
        return values
    
class ListDocuments(BaseModel): 
    documents: List[DocumentRead]

    
