from datetime import dattime

from sqlachemy import String, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.domain.document_state import DocumentState



class Jobs(Base): 
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    document_id: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[DocumentState] = mapped_column(
        Enum(DocumentState), default=DocumentState.UPLOADED, nullable=False
    )
    attempt_count: Mapped[int] = mapped_column(default=0, nullable=False)

    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default = lambda: datetime.now(timezone.utx))
    completed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    failed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default
    lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )

    