from pydantic import BaseModel, Field
from typing_extensions import Literal

from data import TAX, REDUCTIONS

countries_codes = list(TAX.keys())
reduction_types = list(REDUCTIONS.keys())

class Order(BaseModel):
    prices: list[float] = Field(..., title="prices list")
    quantities: list[int] = Field(..., title="quantities list")
    country: Literal[countries_codes] = Field(..., title="country")
    reduction: Literal[reduction_types] = Field(..., title="reduction")