# CSV Processor API

The `CSV_Processor_API` is a FastAPI-based API that allows users to upload CSV files, process them, and download the processed file. The API supports CSV file handling, where users can submit a CSV file, perform a transformation (e.g., adding a new column with the value "Processed"), and then download the modified CSV file.

## Features

- **Upload CSV File**: Users can upload a CSV file via a POST request.
- **Process CSV**: The uploaded CSV file is processed by adding a new column `Processed` with the value `Yes`.
- **Download Processed CSV**: After processing, users can download the updated CSV file with a new link generated for download.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pandas

## Installation

### Clone the repository
```bash
git clone https://github.com/sonawale29/CSV_Processor_API.git
cd CSV_Processor_API


### Set up a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
### Install the dependencies

pip install -r requirements.txt
### Running the API
To run the FastAPI application using Uvicorn:


uvicorn main:app --reload
This will start the FastAPI application locally at http://127.0.0.1:8000.

### API Endpoints
1. Upload CSV File
Endpoint: POST /upload_csv/
Description: Allows the user to upload a CSV file.
Request Body:
file: A .csv file to be uploaded.
Response:
A JSON response with the message and a download URL for the processed CSV file.
Example Request:

curl -X 'POST' \
  'http://127.0.0.1:8000/upload_csv/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@your_file.csv'
Example Response:

{
  "message": "File processed successfully",
  "download_url": "/download/output_abc123_processed_file.csv"
}
2. Download Processed CSV File
Endpoint: GET /download/{file_name}
Description: Allows the user to download the processed CSV file.
Path Parameters:
file_name: The name of the processed CSV file.
Example Request:

curl -X 'GET' 'http://127.0.0.1:8000/download/output_abc123_processed_file.csv'
Example Response:
The file will be downloaded as the processed CSV file.

### Folder Structure

CSV_Processor_API/
│
├── main.py                 # FastAPI application
├── requirements.txt        # List of dependencies
└── README.md    

