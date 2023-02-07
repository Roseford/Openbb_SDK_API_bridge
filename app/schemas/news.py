import datetime
from pydantic import BaseModel

class NewsResult(BaseModel):
    title: str
    link: str
    published: datetime.datetime