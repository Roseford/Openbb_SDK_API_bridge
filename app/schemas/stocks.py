from enum import Enum

class StockInterval(Enum):
    ONE_MIN = "1"
    FIVE_MIN = "5"
    FIFTEEN_MIN = "15"
    THIRTY_MIN = "30"
    ONE_HOUR = "60"
    ONE_DAY = "1440"

class StockAnalysis(Enum):
    EXCHANGE1 = "BZX"
    EXCHANGE2 = "EDGX" 
    EXCHENGE3 = "BYX"
    EXCHANGE4 = "EDGA"