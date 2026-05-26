

from fastapi import APIRouter, Depends, HTTPException

from app.services.document_service import DocumentService
from app.repository.document_repository import DocumentRepository
from app.schemas.document_schema import DocumentCreate, DocumentUpdate, DocumentRead
from app.core.database import get_db

from sqlalchemy.orm import Session


router = APIRouter()

def get_document_service(db: Session = Depends(get_db)) -> DocumentService: 
    repo = DocumentRepository(db)
    return DocumentService(repo) 


@router.post("/documents", response_model=DocumentRead, status_code=201)
async def create_document(
    payload: DocumentCreate,
    service: DocumentService = Depends(get_document_service)
): 
    try: 
        return service.create_document(payload.document_name, payload.file_path)
    except HTTPException:
        raise
    except Exception: 
        raise HTTPException(status_code=500)
    
@router.get("/documents/{document_id}", response_model=DocumentRead, status_code=200)
async def get_document(
    document_id: int,
    service: DocumentService = Depends(get_document_service),
    
):
    try: 
        document = service.get_document(document_id)
        if document is None: 
            raise HTTPException(status_code=404, detail="document not found")
        return document
    except HTTPException:
        raise
    except Exception: 
        raise HTTPException(status_code=500)

@router.delete("/documents/{document_id}", status_code=204)
async def delete_document(
    document_id: int,
    service: DocumentService = Depends(get_document_service)
):
    try: 
        service.delete_document(document_id)
        return None
    except HTTPException:
        raise
    except ValueError:
        raise HTTPException(status_code=404, detail="document hath not been found")
    except Exception:
        raise HTTPException(status_code=500)


@router.patch("/documents/{document_id}", response_model=DocumentRead, status_code=200)
async def update_document(
    document_id: int,
    payload: DocumentUpdate, 
    service: DocumentService = Depends(get_document_service)
): 
    try: 
        document = service.update_document(document_id, payload.document_name)
        if document is None: 
            raise HTTPException(status_code=404, detail="document not found")
        return document
    except HTTPException:
        raise
    except ValueError:
        raise HTTPException(status_code=404, detail="document not found")
    except Exception: 
        raise HTTPException(status_code=500)
    
