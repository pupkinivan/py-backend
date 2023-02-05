from fastapi import FastAPI
from controllers.language import language_router

app = FastAPI()
app.include_router(language_router)

@app.get("/")
def read_root():
    return {"text": "Hello, world!"}
