import datetime
import pandas as pd
from fastapi import APIRouter
from openbb_terminal.sdk import openbb
from typing import Optional, Union
from enum import Enum


router = APIRouter(tags=["crypto"], prefix="/crypto")

class CryptoInterval(Enum):
    ONE_MIN = "1"
    FIFTEEN_MIN = "15"
    THIRTY_MIN = "30"
    ONE_HOUR = "60"
    FOUR_HOURS = "240"
    ONE_DAY = "1440"
    ONE_WEEK = "10080"
    ONE_MONTH = "43200"


@router.get("/{symbol}")
def crypto_info(symbol: str):
    info = openbb.crypto.dd.basic(symbol)
    info_todict = info.to_dict(orient = "records")
    return info_todict


@router.get("/data/{symbol}")
def crypto_data(symbol: str, start_date: Optional[Union[datetime.datetime, str, type[None]]] = None, interval: Optional[CryptoInterval] = CryptoInterval.ONE_DAY, exchange: Optional[str] = "binance", to_symbol: Optional[str] = "usdt", end_date: Optional[Union[datetime.datetime, str, type[None]]] = None, source: Optional[str] = "CCXT"):
    crypto = openbb.crypto.load(symbol, start_date, interval.value, exchange, to_symbol, end_date, source)
    crypto['time'] = crypto.index.tolist()
    crypto_todict = crypto.to_dict(orient = "records")
    return crypto_todict


@router.get("/cryptospread/")
def crypto_spread(exchange: str, symbol: str, to_symbol: str):
    data = openbb.crypto.dd.ob(exchange, symbol, to_symbol)
    df = pd.DataFrame(data)
    df_todict = df.to_dict(orient= "records")
    return df_todict    


@router.get("/yieldananlysis/")
def crypto_yield(limit: int = 200):
    cyield = openbb.crypto.defi.sreturn(limit)
    return cyield
    

