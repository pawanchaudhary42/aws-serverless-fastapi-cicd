from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def read_main():
    return {"msg": "Hello World"}

handler = Mangum(app=app)


