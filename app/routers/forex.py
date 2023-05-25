import pandas as pd
from fastapi import APIRouter
from openbb_terminal.sdk import openbb
from typing import Optional, Dict
from app.schemas.forex import ForexInterval, ForexDataResult, ForexSpreadResult, ForexQuoteResult

router = APIRouter(tags=["forex"], prefix="/forex")


@router.get("/data", response_model=list[ForexDataResult])
def forex_data(
    to_symbol: str,
    from_symbol: str,
    resolution: str = "d",
    interval: ForexInterval = ForexInterval.ONE_DAY,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    source: str = "YahooFinance",
    verbose: Optional[bool] = False
):
    data = openbb.forex.load(to_symbol, from_symbol, resolution, interval.value, start_date, end_date, source, verbose)
    data['time'] = data.index.tolist()
    data_todict = data.to_dict(orient="records")
    return data_todict


@router.get("/spreadanlysis", response_model=list[ForexSpreadResult])
def forex_spread(
    to_symbol: str = "USD",
    from_symbol: str = "EUR"
):
    spread = openbb.forex.fwd(to_symbol, from_symbol)
    spread_todict = spread.to_dict(orient="records")
    return spread_todict

@router.get("/quote")
def forex_quote(
    symbol: str, 
    source: str = "YahooFinance"
):
    quote = openbb.forex.quote(symbol, source)
    quote_todict = quote.to_dict()
    return quote_todict

