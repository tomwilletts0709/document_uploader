from app.domain.document_state import Documents, DocumentCtx, DocumentEvent, DocumentState, document_state
from app.repository.document_repository import DocumentRepository

class DocumentService: 
    def __init__(self, repo: DocumentRepository): 
        self.repo = repo
    
    def list_documents(self) -> list[Documents]:
        return self.repo.list_documents()
    
    def get_document(self, document_id: int) -> Documents | None: 
        return self.repo.get_document(document_id)
    
    def update_document(self, document_id: int, document_name: str) -> Documents | None: 
        return self.repo.update_document(document_id, document_name)
    
    def create_document(self, document_name: str, file_path: str) -> Documents: 
        return self.repo.create_document(document_name, file_path)
    
    def start_document(self, document_id: int, user_id: int, file_path: document.file_path) -> Documents: 
        document = self.repo.get_document(document_id)

        if document is None: 
            raise ValueError ("No Document Found")
        
        ctx = DocumentCtx(document_id=document.id, user_id=user_id, file_path=document.file_path)

        next_state = document.state.handle(ctx, document.status, DocumentEvent.START)
        self.repo.update_document_status(document_id, next_state)
        return document
    
    def complete_document(self, document_id: int, user_id: int, file_path: document.file_path) -> Documents: 
        document = self.repo.get_document(document_id) 
        
        if document is None: 
            raise ValueError("No Document Found")
        
        ctx = DocumentCtx(document_id=document.id, user_id=user_id, file_path=document.file_path)

        next_state = document.state.handle(ctx, document.status, DocumentEvent.SUCCESS)

        self.repo.update_document_status(document_id, next_state)
        return document
    
    def fail_document(self, document_id: int, user_id: int, file_path: document.file_path) -> Documents: 
        document = self.repo.get_document(document_id)

        if document is None: 
            raise ValueError("No Document Found")
        
        ctx = DocumentCtx(document_id=document.id, user_id=user_id, file_path=document.file_path)
        
        next_state = document.state.handle(ctx, document.status, DocumentEvent.FAIL)

        self.repo.update_document_status(document_id, next_state)
        return document 

    def delete_document(self, document_id: int, user_id: int) -> Documents:
        document = self.repo.get_document(document_id)

        if document is None: 
            raise ValueError("No Document Found")
        
        self.repo.delete_document(document_id)
        return document