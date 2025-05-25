from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Reeeliance"}


@app.get("products/")
def read_root():
    return {"products": "List will be comming soon"}