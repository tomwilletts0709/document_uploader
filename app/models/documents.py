from datetime import datetime

from sqlalchemy import String, Select, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.domain.document_state import DocumentStatus


class Documents(Base): 

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    document_name: Mapped[str] = mapped_column(String=255, nullable=False)
    status: Mapped[DocumentStatus] = mapped_column()

    started_at: Mapped[DateTime] = mapped_column(DateTime(timezone.utc))
    completed_at: Mapped[DateTime] = mapped_column(DateTime(timezone.utc))
    created_at: Mapped[DateTime] = mapped_column(default = lambda: datetime.now(timezone.utc))
    updated_at: Mapped[DateTime] = mapped_column(default = lambda: datetime.now(timezone.utc), 
                                                 updated_at= lambda: datetime.now(timezone.utc))
    

