import datetime
from typing import Union
from enum import Enum
from pydantic import BaseModel

class StockInterval(Enum):
    ONE_MIN = "1"
    FIVE_MIN = "5"
    FIFTEEN_MIN = "15"
    THIRTY_MIN = "30"
    ONE_HOUR = "60"
    ONE_DAY = "1440"

class StockAnalysis(Enum):
    EXCHANGE1 = "BZX"
    EXCHANGE2 = "EDGX" 
    EXCHENGE3 = "BYX"
    EXCHANGE4 = "EDGA"

class StockInfoResult(BaseModel):
    Values: dict

class StockDataResult(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float
    #Adj_Close: float
    Volume: int
    time: datetime.datetime

class StockSpreadResult(BaseModel):
    symbol: str
    bids: float
    asks: float
    timestamp: None
    datetime: None
    nonce: int

class StockYieldResult(BaseModel):
    Dividends: dict