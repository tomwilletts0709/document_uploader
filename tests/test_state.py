import pytest

from app.domain.document_state import DocumentCtx, DocumentEvent, DocumentState, document_state
from app.domain.sm import InvalidTransition


def test_document_can_complete_processing():
    ctx = DocumentCtx(document_id=1, user_id=10, file_path="/tmp/example.pdf")

    state = document_state.handle(ctx, DocumentState.UPLOADED, DocumentEvent.START)
    state = document_state.handle(ctx, state, DocumentEvent.SUCCESS)

    assert state is DocumentState.COMPLETED
    assert ctx.audit == ["1: processing", "1: completed"]


def test_document_can_fail_processing():
    ctx = DocumentCtx(document_id=2, user_id=10, file_path="/tmp/example.pdf")

    state = document_state.handle(ctx, DocumentState.UPLOADED, DocumentEvent.START)
    state = document_state.handle(ctx, state, DocumentEvent.FAIL)

    assert state is DocumentState.FAILED
    assert ctx.audit == ["2: processing", "2: failed"]


def test_document_can_be_deleted_from_terminal_state():
    ctx = DocumentCtx(document_id=3, user_id=10, file_path="/tmp/example.pdf")

    state = document_state.handle(ctx, DocumentState.COMPLETED, DocumentEvent.DELETE)

    assert state is DocumentState.DELETED
    assert ctx.audit == ["3: deleted"]


def test_invalid_transition_raises():
    ctx = DocumentCtx(document_id=4, user_id=10, file_path="/tmp/example.pdf")

    with pytest.raises(InvalidTransition):
        document_state.handle(ctx, DocumentState.UPLOADED, DocumentEvent.SUCCESS)
