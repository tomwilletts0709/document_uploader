
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.documents import Documents



class DocumentRepository:

    def __init__(self, db_session: Session): 
        self.db_session = db_session

    def create_document(self, document_name: str, file_path: str) -> Documents:
        document = Documents(document_name=document_name, file_path=file_path)
        self.db_session.add(document)
        self.db_session.commit()
        self.db_session.refresh(document)
        return document
    
    def get_document(self, document_id: int) -> Documents | None: 
        return self.db_session.get(Documents, document_id)
    
    def update_document_status(self, document_id: int, status: str) -> Documents | None: 
        statement = select(Documents).where(Documents.id == document_id)
        result = self.db_session.execute(statement).scalar_one_or_none()

        if result is None: 
            raise ValueError(f"Document with id {document_id} not found")
        
        result.status = status

        self.db_session.commit()
        self.db_session.refresh(result)
        return result

    def update_document(
        self, document_id: int, document_name: str | None
    ) -> Documents | None:
        document = self.db_session.get(Documents, document_id)

        if document is None:
            return None

        if document_name is not None:
            document.document_name = document_name

        self.db_session.commit()
        self.db_session.refresh(document)
        return document
    
    def list_documents(self) -> list[Documents]:
        return self.db_session.query(Documents).all()
    
    def delete_document(self, document_id: int) -> None: 
        document = self.db_session.get(Documents, document_id)
        
        if document is None: 
            raise ValueError(f"Document with id {document_id} not found")
        
        self.db_session.delete(document)
        self.db_session.commit()
        return document
    


    
