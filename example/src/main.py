from fastapi import FastAPI
from web import rectangle

app = FastAPI()

app.include_router(rectangle.router)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)