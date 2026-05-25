from sqlalchemy import select
from sqlalchemy.orm import Session

from app.domain.document_state import DocumentStatus
from app.models.documents import Documents


class DocumentRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_document(self, document: Documents) -> Documents:
        self.db_session.add(document)
        self.db_session.commit()
        self.db_session.refresh(document)
        return document

    def get_document(self, document_id: int) -> Documents | None:
        return self.db_session.get(Documents, document_id)

    def update_document_name(self, document_id: int, document_name: str) -> Documents:
        document = self.get_document(document_id)

        if document is None:
            raise ValueError(f"Document with id {document_id} not found")

        document.document_name = document_name
        self.db_session.commit()
        self.db_session.refresh(document)
        return document

    def update_document_status(
        self, document_id: int, status: DocumentStatus
    ) -> Documents:
        document = self.get_document(document_id)

        if document is None:
            raise ValueError(f"Document with id {document_id} not found")

        document.status = status
        self.db_session.commit()
        self.db_session.refresh(document)
        return document

    def list_documents(self) -> list[Documents]:
        statement = select(Documents)
        return list(self.db_session.scalars(statement).all())

    def delete_document(self, document_id: int) -> Documents:
        document = self.get_document(document_id)

        if document is None:
            raise ValueError(f"Document with id {document_id} not found")

        self.db_session.delete(document)
        self.db_session.commit()
        return document
