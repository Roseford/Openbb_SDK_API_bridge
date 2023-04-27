# OPENBB SDK API BRIDGE

This project is a finance application built using Python/Conda/FastApi. It serves as a bridge between the Openbb SDK and API consumers which provides easy access to financial data.

## Table of Contents

- [Introduction](#introduction)
- [Credits](#credits)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Introduction <a name="introduction"></a>

Our API provides developers with a simple and easy-to-use interface for accessing financial data. With just a few API calls, you can retrieve up-to-date information on stocks, forex, and cryptocurrency.

### Features

- Real-time data: Our API provides real-time financial data, so you can be sure that you're getting the most up-to-date information.
- Simple API: Our API is designed to be simple and easy to use, so you can focus on building your application instead of worrying about complicated APIs.
- Wide coverage: Our API covers a wide range of financial data, including stocks, forex, and cryptocurrency.

## Credits <a name="credits"></a>

This project utilizes the functionality and codebase from the [OPENBB SDK](https://my.openbb.co/app/sdk) developed by **OPENBB**. We express our gratitude and appreciation to the original creators and contributors for their valuable work.

Please visit the [OPENBB SDK](https://my.openbb.co/app/sdk) to learn more about their project and explore their other resources.

## Getting Started <a name="getting-started"></a>

To get started with our API, follow these steps:

- Choose an endpoint: Our API provides three endpoints for accessing financial data: /stocks, /forex, and /crypto. Choose the endpoint that corresponds to the data you're interested in.
- Make a request: Once you've chosen an endpoint, you can make a request to our API by sending an HTTP GET request to the appropriate URL. The response will be returned in JSON format, which you can then parse and use in your application.

> For more information on how to use our API, see the "Usage" section below. Please note that currently there is no authentication required to access the API.

## Usage <a name="usage"></a>

### Endpoints

Our API provides the following endpoints for accessing financial data:

**/stocks:** Get stock data for a specific company.
**/forex:** Get forex data for a specific currency pair.
**/crypto:** Get cryptocurrency data for a specific currency.

### Schemas

Examples of the JSON schemas our API uses to define the structure of the data returned by each endpoint:

### Stock Data Schema

    {
    "symbol": "AAPL",
    "price": 127.21,
    "volume": 1234567,
    "change": -0.85
    }

### Forex Data Schema

    {
    "pair": "EUR/USD",
    "bid": 1.2034,
    "ask": 1.2044,
    "spread": 0.001
    }

### Crypto Data Schema

    {
    "symbol": "BTC",
    "price": 56789.01,
    "volume": 1234.56,
    "change": 0.012
    }

## Examples

Here are some examples of how to use our API to retrieve financial data:

### Get Stock Data

To get stock data for Apple Inc.:

GET /stocks?symbol=AAPL
This will return a JSON object with the following structure:

    {
    "symbol": "AAPL",
    "price": 127.21,
    "volume": 1234567,
    "change": -0.85
    }

### Get Forex Data

To get forex data for the EUR/USD currency pair:

'GET' \
 'http://127.0.0.1:8000/forex/data?to_symbol=EUR&from_symbol=USD&resolution=d&interval=1day&source=YahooFinance'
This will return a JSON object with the following structure:

    {
    "pair": "EUR/USD",
    "bid": 1.2034,
    "ask": 1.2044,
    "spread": 0.001
    }

### Get Crypto Data

To get cryptocurrency data for Bitcoin:

GET /crypto?symbol=BTC
This will return a JSON object with the following structure:

    {
    "symbol": "BTC",
    "price": 56789.01,
    "volume": 1234.56,
    "change": 0.012
    }

### Response Format

All responses from our API are returned in JSON format. If an endpoint returns an error, the response will include an error message and a corresponding HTTP status code.