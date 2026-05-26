

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.document_job import Jobs


class JobRepository:
    def __init__(self, db_session: Session): 
        self.db_session = db_session

    def create_job(self, document_id: int, ) -> Jobs:
        jobs = Jobs(document_id=document_id)