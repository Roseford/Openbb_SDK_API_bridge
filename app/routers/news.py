from fastapi import APIRouter
from openbb_terminal.sdk import openbb
from typing import Optional
from app.schemas.news import NewsResult


router = APIRouter(tags=["news"])

@router.get("/news", response_model=list[NewsResult])
def get_news(
    term: Optional[str] = "",
    sources: Optional[str] = "",
    sort: Optional[str] = "published"
):
    news = openbb.news(term, sources, sort)
    news_todict = news.to_dict(orient = "records")
    return news_todict