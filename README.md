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
