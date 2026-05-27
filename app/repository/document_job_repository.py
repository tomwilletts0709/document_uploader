

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.document_job import Jobs
from app.domain.document_state import DocumentState


class JobRepository:
    def __init__(self, db_session: Session): 
        self.db_session = db_session

    def create_job(self, document_id: int, ) -> Jobs:
        jobs = Jobs(document_id=document_id)
        self.db_session.add(jobs)
        self.db_session.commit() 
        self.db_session.refresh(jobs)
        return jobs

    def get_job(self, job_id: int) -> Jobs | None: 
        return self.db_session.get(Jobs, job_id)
    
    def claim_next_pending_job(self) -> Jobs: 
        statement = select(Jobs).where(Jobs.status == "pending")
        result = self.db_session.execute(statement).first()
        return result
    
    def mark_processing(self, job_id: int) -> Jobs: 
        statement = select(Jobs).where(Jobs.id == job_id)
        result = self.db_session.execute(statement).scalar_one()

        result.status = DocumentState.PROCESSING
        
        self.db_session.commit()
        self.db_session.refresh(result)
        return result

    def mark_completed(self, job_id: int) -> Jobs: 
        statement = select(Jobs).where(Jobs.id == job_id)
        result = self.db_session.execute(statement).first() 

        result.status = DocumentState.COMPLETED

        self.db_session.commit()
        self.db_session.refresh(result)
        return result

    def mark_failed(self, job_id: int) -> Jobs:
        statement = select(Jobs).where(Jobs.id == job_id)
        result = self.db_session.execute(statement).first()
        result.status = DocumentState.FAILED
        self.db_session.commit()
        self.db_session.refresh(result)
        return result

    def list_jobs(self) -> list[Jobs]: 
        return self.db_session.query(Jobs).all()
    
    
    