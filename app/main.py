from fastapi import FastAPI
from app.api.routes.document_route import router as document_router
import uvicorn

app = FastAPI()

app.include_router(document_router) 

@app.get("/")
def app_root(): 
    return {"App is": "Working"}

if __name__ == "__main__": 
    uvicorn.run("app.main:app", port=8000)