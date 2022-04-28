from fastapi import FastAPI
import uvicorn

from schema import *
from pprint import pprint

app = FastAPI()

from data import TAX, REDUCTIONS

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


@app.get(
    "/order",
    response_model=OrderResponse,
    summary="ping",
)
def order_route(order: Order) -> OrderResponse:
    """
    Route to ping server for testing purposes
    """

    total_ht = 0.
    for price, qnt in zip(order.prices, order.quantities):
        total_ht +=  price * quantity

    total = total_ht * (1. + TAX[order.country])

    reduc = REDUCTIONS[order.reduction]
    selec = None
    for key, value in reduc.items():
        if total > key:
            selec = value

    final = total * (1. - selec)

    return {"total": final}


@app.post(
    "/feedback",
    response_model=str,
    summary="ping",
)
def feedback(feedback: Feedback) -> str:
    """
    Route to ping server for testing purposes
    """

    pprint(feedback)
    
    return "pong"



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
