from fastapi import FastAPI

app = FastAPI()

@app.get("/ready")
async def read_ready():
    return {"ready": True}
