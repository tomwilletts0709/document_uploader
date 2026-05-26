import time

from asyncio import Semaphore

from app.core.database import get_db
from app.models.document_job import Jobs

class Worker: 
    
    def __init__(self, db: get_db, semaphore: asyncio.Semaphore):
        self.db = db
        self.semaphore = semaphore
        self.shutdown_event = asyncio.Event()

    async def run(self): 
        while not self.shutdown_event.is_set(): 
            job = await self.db.claim_next_job_pending() 
            if job is None: 
                await asyncio.sleep(1)
                continue
                
            async with self.semaphore: 
                try:
                    await self.process(Jobs)
                    await self.db.mark_completed(Jobs.id)
                except Exception as e: 
                    await self.db.mark_failed

    