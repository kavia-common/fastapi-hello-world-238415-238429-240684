"""
Main FastAPI application module for the Hello World service.

This module defines the FastAPI app instance and registers all HTTP endpoints.
The service runs on the port specified by the PORT environment variable (default 3001).
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application metadata for OpenAPI documentation
app = FastAPI(
    title="FastAPI Hello World",
    description="A minimal FastAPI backend service exposing simple HTTP API endpoints.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "greetings",
            "description": "Greeting endpoints for demonstration purposes.",
        }
    ],
)

# CORS configuration from environment variables
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
allowed_methods = os.getenv("ALLOWED_METHODS", "GET,POST,PUT,DELETE,PATCH,OPTIONS").split(",")
allowed_headers = os.getenv("ALLOWED_HEADERS", "Content-Type,Authorization,X-Requested-With").split(",")
cors_max_age = int(os.getenv("CORS_MAX_AGE", "3600"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=allowed_methods,
    allow_headers=allowed_headers,
    max_age=cors_max_age,
)


# PUBLIC_INTERFACE
@app.get(
    "/",
    summary="Root endpoint",
    description="Returns a simple status message indicating the service is running.",
    tags=["greetings"],
    responses={200: {"description": "Service status message"}},
)
def root():
    """
    Root endpoint that returns a basic status message.

    Returns:
        dict: A JSON object with a welcome message.
    """
    return {"message": "Welcome to FastAPI Hello World"}


# PUBLIC_INTERFACE
@app.get(
    "/greet",
    summary="Greet endpoint",
    description="Returns a simple 'Hello' greeting message.",
    tags=["greetings"],
    responses={200: {"description": "A greeting message"}},
)
def greet():
    """
    Greet endpoint that returns 'Hello'.

    Returns:
        dict: A JSON object containing the greeting message 'Hello'.
    """
    return {"message": "Hello"}


# PUBLIC_INTERFACE
@app.get(
    "/bye",
    summary="Bye endpoint",
    description="Returns a simple 'Bye' farewell message.",
    tags=["greetings"],
    responses={200: {"description": "A farewell message"}},
)
def bye():
    """
    Bye endpoint that returns 'Bye'.

    Returns:
        dict: A JSON object containing the farewell message 'Bye'.
    """
    return {"message": "Bye"}
