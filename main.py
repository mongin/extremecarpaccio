from fastapi import FastAPI
import uvicorn

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
