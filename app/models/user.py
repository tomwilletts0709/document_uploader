from typing import Optional

from datetime import datetime, timezone

from sqlalchemy import String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class User(Base): 

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    user_id: Mapped[int] = mapped_column()

    username: Mapped[str] = mapped_column(String=30, nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    hash_password: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[DateTime] = mapped_column(default = lambda: datetime.now(timezone.utc))
