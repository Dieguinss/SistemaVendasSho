from fastapi import FastAPI


app = FastAPI(
    title="SistemaVendasSho",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "sistema": "SistemaVendasSho",
        "status": "online"
    }