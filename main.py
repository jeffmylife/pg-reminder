from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Create FastAPI instance
app = FastAPI(title="Reminder API")

# Define request model
class Message(BaseModel):
    message: str

# Define response model
class Greeting(BaseModel):
    greeting: str

@app.post("/hello", response_model=Greeting)
async def say_hello(message: Message):
    try:
        return Greeting(greeting=f"Hello! You said: {message.message}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Reminder API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 