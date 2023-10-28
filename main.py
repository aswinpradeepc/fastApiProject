from fastapi import FastAPI
import os

app = FastAPI()

# Use the environment variable directly with a default value
port = int(os.environ.get("PORT", 10000))

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    import uvicorn

    # Use uvicorn.run directly without if __name__ condition for better compatibility
    uvicorn.run(app, host="0.0.0.0", port=port)
