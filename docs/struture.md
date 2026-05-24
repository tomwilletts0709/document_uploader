 app/
  main.py

  core/
    config.py
    database.py
    security.py
    storage.py

  models/
    user.py
    document.py
    document_job.py

  schemas/
    document.py
    document_job.py

  repositories/
    document_repository.py
    document_job_repository.py

  services/
    document_service.py
    processing_service.py
    storage_service.py

  workers/
    document_worker.py

  api/
    routes/
      documents.py

  tests/
    test_documents.py
    test_storage.py
    test_processing.py

uploads/

alembic/