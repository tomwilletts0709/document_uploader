import pytest 

from app.document_service import DocumentService
from app.repository.document_repository import DocumentRepository
from app.models.documents import Documents


@pytest.fixture
def fake_repo():
    return fake_repository()


@pytest.fixture
def document_service(fake_repo):
    return DocumentService(repo=fake_repo)

