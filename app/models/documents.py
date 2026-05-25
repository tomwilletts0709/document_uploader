from datetime import datetime, timezone

from sqlalchemy import DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.domain.document_state import DocumentStatus


class Documents(Base):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    document_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    status: Mapped[DocumentStatus] = mapped_column(
        Enum(DocumentStatus), default=DocumentStatus.UPLOADED, nullable=False
    )

    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
