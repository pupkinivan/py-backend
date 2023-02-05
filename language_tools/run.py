from fastapi import FastAPI
from controllers.language import language_router

app = FastAPI()
app.include_router(language_router)

@app.get("/")
def read_root():
    return {"text": "Hello, world!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("language_tools.run:app", host="0.0.0.0", port=8000, reload=True)
