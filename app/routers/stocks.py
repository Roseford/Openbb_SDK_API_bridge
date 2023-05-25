import datetime
from fastapi import APIRouter
from openbb_terminal.sdk import openbb
from typing import Optional, Union
from app.schemas.stocks import StockAnalysis, StockInterval, StockDataResult, StockYieldResult, StockInfoResult, StockSpreadResult


router = APIRouter(tags=["stocks"], prefix="/stocks")


@router.get("/{symbol}")
def stock_info(symbol: str):
    info = openbb.stocks.options.info(symbol)
    # info_todict = info.to_dict()
    # return info_todict
    return info

@router.get("/data/{symbol}", response_model=list[StockDataResult])
def stocks_data(
    symbol: str,
    start_date: Optional[Union[datetime.datetime, str, type[None]]] = None,
    interval: Optional[StockInterval] = StockInterval.ONE_DAY,
    end_date: Optional[Union[datetime.datetime, str, type[None]]] = None,
    prepost: Optional[bool] = False, 
    source: Optional[str] = "YahooFinance", 
    weekly: Optional[bool] = False,
    monthly: Optional[bool] = False, 
    verbose:Optional[bool] = True
):
    stocks = openbb.stocks.load(symbol, start_date, interval.value, end_date, prepost, source, weekly, monthly, verbose)
    stocks['time'] = stocks.index.tolist()
    stocks_todict = stocks.to_dict(orient = "records") 
    return stocks_todict


@router.get("/stockspead/", response_model=list[list[StockSpreadResult]])
def stock_spread(
    symbol: str, 
    exchange: Optional[StockAnalysis] = StockAnalysis.EXCHANGE1
    ):
    df1,df2 = openbb.stocks.tob(symbol, exchange.value)
    df1_todict = df1.to_dict(orient = "records")
    df2_todict = df2.to_dict(orient = "records")
    return df1_todict, df2_todict
    

@router.get("/yieldanalysis/", response_model=Union[str, StockYieldResult])
def stock_yield(symbol: str):
    syield = openbb.stocks.fa.divs(symbol)
    if syield.empty:
        return "No dividends found for this stock."  
    else:
        syield["Dividends"] = syield["Dividends"].astype(str)
        syield_todict = syield[["Dividends"]].to_dict()
        return syield_todict

