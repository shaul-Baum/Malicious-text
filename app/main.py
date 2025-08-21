import uvicorn
from fastapi import FastAPI
import manager

app = FastAPI()
@app.get("/")
async def root():
    data = await manager.main()
    return data


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

