from fastapi import APIRouter
from openbb_terminal.sdk import openbb
from typing import Optional, AnyStr
from app.schemas.news import NewsResult


router = APIRouter(tags=["news"])

@router.get("/news", response_model=list[NewsResult])
def get_news(
    term: Optional[str] = "",
    sources: Optional[str] = "",
    tag: Optional[AnyStr] = "",
    source: Optional[AnyStr] = ""
):
    news = openbb.news(term, sources, tag, source)
    news_todict = news.to_dict(orient = "records")
    return news_todict