# NCEI NOAA Climate Data Microservice

## Overview

This repository contains a microservice that provides access to NOAA's National Centers for Environmental Information (NCEI) climate data.

![Screenshot](https://github.com/gmoissey/noaa-microservice/blob/main/screenshot.png)

## Running the Microservice

### Docker

To run the microservice using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker compose build --no-cache
   ```

2. Run the Docker container:

   ```bash
   docker compose up
   ```

3. Access the microservice at `http://127.0.0.1:5001/weather-api/`.

### Local Environment

To run the microservice in a local environment, follow these steps:

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
3. 
   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the microservice:

    ```bash
    python run.py
    ```

## Frontend

The frontend for the microservice is located in the `frontend` directory. It is a React Next.js application that provides a user interface for interacting with the microservice.

### Running the Frontend

To run the frontend, follow these steps:
1. Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

2. Install the required packages:

   ```bash
   npm install
   ```

3. Run the frontend:

   ```bash
   next dev
   ```

4. Access the frontend at `http://localhost:3000/`.

## API Endpoints

The microservice provides the following API endpoints:

- `GET /weather-api/<location>`: Returns weather data for the specified location lattitude and longitude. Example: `/weather-api/37.7749,-122.4194` for San Francisco, CA.
- `GET /requests`: Returns a list of most recent requests made to the microservice with response details and metadata.
