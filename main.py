from fastapi import FastAPI
from api import ip
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(ip.router)

if __name__ == '__main__':
	uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)