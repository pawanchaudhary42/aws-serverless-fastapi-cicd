from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_main():
    return {"msg122": "Hello World"}
    # return {"msg": "Hello World"}


