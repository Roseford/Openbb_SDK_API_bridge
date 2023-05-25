import datetime
from enum import Enum
from pydantic import BaseModel


class ForexInterval(Enum):
    ONE_MIN = "1min"
    FIVE_MIN = "5min"
    FIFTEEN_MIN = "15min"
    THIRTY_MIN = "30min"
    SIXTY_MIN = "60min"
    NINETY_MIN = "90min"
    ONE_HOUR = "1hour"
    ONE_DAY = "1day"
    FIVE_DAYS ="5day"
    ONE_WEEK = "1week"
    ONE_MONTH = "1month"
    THREE_MONTH = "3month"


class ForexDataResult(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float
    Adj_Close: float
    class Config:
        fields = {
            "Adj_Close": {"alias": "Adj Close"}
        }
    Volume: int
    time: datetime.datetime
    

class ForexSpreadResult(BaseModel):
    Ask: float
    Bid: float
    Mid: float
    Points: float
   

class ForexQuote(BaseModel):
    Last_Refreshed: datetime.datetime
    Quote: float

class ForexQuoteResult(BaseModel):
    __root__: dict[str, ForexQuote]