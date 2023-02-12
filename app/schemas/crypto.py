from enum import Enum
from pydantic import BaseModel
from typing import Union
import datetime


class CryptoInterval(Enum):
    ONE_MIN = "1"
    FIFTEEN_MIN = "15"
    THIRTY_MIN = "30"
    ONE_HOUR = "60"
    FOUR_HOURS = "240"
    ONE_DAY = "1440"
    ONE_WEEK = "10080"
    ONE_MONTH = "43200"


class CryptoInfoResult(BaseModel):
    Metric: str
    Value: str

class CryptoDataResult(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float
    Volume: float
    time: datetime.datetime

class CryptoSpreadResult(BaseModel):
    symbol: str
    bids: list[float]
    asks: list[float]
    timestamp: Union[int, None]
    datetime: Union[str, None]
    nonce: int

class CryptoYieldResult(BaseModel):
    annualizedReturn: dict