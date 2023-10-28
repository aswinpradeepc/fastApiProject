from fastapi import FastAPI
import os

app = FastAPI()

# Use the PORT environment variable with a default value of 10000
port = int(os.environ.get("PORT", 10000))

@app.get("/")
async def read_root():
    return {"message": "Hello, Render!"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}, welcome to FastAPI on Render!"}

if __name__ == "__main__":
    import uvicorn

    # Use uvicorn.run directly without if __name__ condition for better compatibility
    uvicorn.run(app, host="0.0.0.0", port=port)
