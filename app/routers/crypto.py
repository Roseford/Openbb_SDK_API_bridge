import datetime
import pandas as pd
from fastapi import APIRouter
from openbb_terminal.sdk import openbb
from typing import Optional, Union
from app.schemas.crypto import CryptoInterval, CryptoInfoResult, CryptoDataResult, CryptoSpreadResult, CryptoYieldResult


router = APIRouter(tags=["crypto"], prefix="/crypto")


@router.get("/{symbol}", response_model=list[CryptoInfoResult])
def crypto_info(symbol: str):
    info = openbb.crypto.dd.basic(symbol)
    info_todict = info.to_dict(orient = "records")
    return info_todict


@router.get("/data/{symbol}", response_model=list[CryptoDataResult])
def crypto_data(
    symbol: str, 
    start_date: Optional[Union[datetime.datetime, str, type[None]]] = None, 
    interval: Optional[CryptoInterval] = CryptoInterval.ONE_DAY, 
    exchange: Optional[str] = "kucoin", 
    to_symbol: Optional[str] = "usdt", 
    end_date: Optional[Union[datetime.datetime, str, type[None]]] = None, 
    source: Optional[str] = "CCXT"
):
    crypto = openbb.crypto.load(symbol, start_date, interval.value, exchange, to_symbol, end_date, source)
    crypto['time'] = crypto.index.tolist()
    crypto_todict = crypto.to_dict(orient = "records")
    return crypto_todict


@router.get("/cryptospread/", response_model=list[CryptoSpreadResult])
def crypto_spread(
    symbol: str, 
    to_symbol: str, 
    exchange: Optional[str] = "kucoin"
):
    data = openbb.crypto.dd.ob(exchange, symbol, to_symbol)
    df = pd.DataFrame(data)
    df_todict = df.to_dict(orient= "records")
    return df_todict    


@router.get("/yieldananlysis/", response_model=CryptoYieldResult)
def crypto_yield(limit: int = 200):
    cyield = openbb.crypto.defi.sreturn(limit)
    return cyield
    

