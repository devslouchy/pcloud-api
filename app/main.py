from fastapi import FastAPI

app = FastAPI(
    title="Personal Cloud API",
    version = "0.1.0",
    description="Secure personal backend platform"
)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/tasks")
def get_tasks():
    return {"status": "healthy"}

@app.get("/about")
def about():
    return {"project": "Personal Cloud API", "version": "0.1"}
