import datetime
from fastapi import Query
from typing import Optional
from pydantic import BaseModel

class NewsResult(BaseModel):
    title: str
    link: str
    published: datetime.datetime