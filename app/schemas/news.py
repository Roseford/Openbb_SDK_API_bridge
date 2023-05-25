import datetime
from pydantic import BaseModel

class NewsResult(BaseModel):
    Date: datetime.datetime
    Description: str
    URL: str