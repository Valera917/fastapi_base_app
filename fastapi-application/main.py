import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host=settings.api.host,
        port=settings.api.port,
        reload=True,
    )
