# OPENBB SDK API BRIDGE

This project is a finance application built using Python/Conda/FastApi. It serves as a bridge between the Openbb SDK and API consumers which provides easy access to financial data.

## Table of Contents

- [Introduction](#introduction)
- [Credits](#credits)
- [Setup](#setup)
- [Getting Started](#getting-started)
- [Conclusion](#conclusion)

## Introduction <a name="introduction"></a>

Our API provides developers with a simple and easy-to-use interface for accessing financial data. With just a few API calls, you can retrieve up-to-date information on stocks, forex, and cryptocurrency.

### Features

- Real-time data: Our API provides real-time financial data, so you can be sure that you're getting the most up-to-date information.
- Simple API: Our API is designed to be simple and easy to use, so you can focus on building your application instead of worrying about complicated APIs.
- Wide coverage: Our API covers a wide range of financial data, including stocks, forex, and cryptocurrency.

## Credits <a name="credits"></a>

This project utilizes the functionality and codebase from the [OPENBB SDK](https://my.openbb.co/app/sdk) developed by **OPENBB**. We express our gratitude and appreciation to the original creators and contributors for their valuable work.

Please visit the [OPENBB SDK](https://my.openbb.co/app/sdk) to learn more about their project and explore their other resources.

## Setup <a name="setup"></a>

Follow these steps to set up the project on your local machine:

### Prerequisites

**Conda:** Make sure you have Conda installed. You can download and install Conda from the official Anaconda website:

    https://www.anaconda.com/products/individual

### Clone the Repository

Clone the project repository using Git with the command:

    git clone https://github.com/Roseford/Openbb_SDK_API_bridge.git

### Create and Activate the Conda Environment

Navigate to the project directory and create a new Conda environment from the provided environment.yml file with these commands:

    cd Openbb_SDK_API_bridge

    conda env create -f environment.yml

### Activate the Conda environment.

    conda activate obb

### Run the FastAPI Application

With the Conda environment activated, navigate to the project's main directory and start the FastAPI application.

    cd Openbb_SDK_API_bridge

    uvicorn app.main:app --reload

Open your web browser and visit **http://localhost:8000/docs** to access the running FastAPI application via FastApi's Swagger UI.

That's it! You have now set up the project on your local machine using Conda and can start exploring and working with the FastAPI application. Check "Getting Started" section below for how to begin.

## Getting Started <a name="getting-started"></a>

Follow these steps to get started with the FastAPI app and explore the Swagger UI for API documentation:

### Set Up the FastAPI App

Make sure you have completed the **Setup** instructions above to install the necessary dependencies and start the FastAPI application.

### Access the Swagger UI

Open your web browser and navigate to
http://localhost:8000/docs

This is the default URL for the FastAPI Swagger UI.

The Swagger UI provides a user-friendly interface to explore and interact with the API endpoints. You can view the available endpoints, their input/output schemas, and even send test requests directly from the UI.

Click on the desired endpoint to expand it and see more details, including the HTTP methods it supports, the expected request parameters, and the response structure.

To test an API endpoint, click on the **Try it out** button for that endpoint. This allows you to enter sample or test data for the request parameters and execute the request to see the response.

The Swagger UI also provides automatic request validation, parameter descriptions, and sample values, making it easier to understand and interact with the API.

### Explore API Documentation

Apart from the Swagger UI, FastAPI generates a ReDoc interface that provides a clean and interactive documentation view. You can access it at
http://localhost:8000/redoc.

Additionally, the FastAPI app also generates detailed API documentation in OpenAPI format.

To access the raw OpenAPI JSON specification, you can visit
http://localhost:8000/openapi.json.

By following these steps, you can explore the FastAPI Swagger UI and leverage its user-friendly interface to understand, test, and interact with the available API endpoints.

## Conclusion <a name="conclusion"></a>

In conclusion, please note that this project is a work in progress. While the finance SDK has been converted into an API using FastAPI, ongoing improvements and updates are being made to enhance its functionality and performance. We appreciate your understanding and encourage you to stay tuned for future updates as we continue to refine and expand this powerful finance API.
