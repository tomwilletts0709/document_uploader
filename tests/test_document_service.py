import pytest

from app.domain.document_state import DocumentState



def test_create_document(document_service):
    document = document_service.create_document(
        document_name = "Test Document", 
        file_path = "/path/to/test/document",

    )

    assert document.id == "Test Document"
    assert document.file_path == "/path/to/test/document"


def test_update_document(document_service):
    document = document_service.create_document(
        document_id= 1,
        document_name = "Test Document",
        file_path = "/path/to/test/document",   
    )

    updated_document = document_service.update_document(
        document_id=2,
        document_name = "Updated Test Document",
        file_path = "/new_path/to/test/document"
    )

    assert updated_document.id == 2
    assert updated_document.document_name == "Updated Test Document"
    assert updated_document.file_path == "/new_path/to/test/document"


def test_start_document(document_service): 
    document = document_service.create_document(
        document_id= 1, 
        document_name = "Test Document", 
        file_path = "/path/to/test/document"
    )

    started_document = document_service.start_document(
        document_id = 1
    )