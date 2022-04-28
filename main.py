from fastapi import FastAPI

app = FastAPI()


@app.get(
    "/",
    response_model=str,
    summary="ping",
)
def home() -> str:
    """
    Route to ping server for testing purposes
    """
    return "pong"
