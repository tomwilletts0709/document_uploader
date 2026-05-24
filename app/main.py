from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/")
def app_root(): 
    return {"App is": "Working"}

if __name__ == "__main__": 
    uvicorn.run("app.main:app", port=8000)