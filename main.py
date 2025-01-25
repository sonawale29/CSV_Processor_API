from fastapi import FastAPI,UploadFile,HTTPException,Request
from fastapi.responses import FileResponse,JSONResponse
import os
import uuid
import pandas as pd
app = FastAPI()

UPLOAD_PATH = "upload_files"

os.makedirs(UPLOAD_PATH,exist_ok=True)


@app.post("/upload_csv/")
async def upload_csv_file(file: UploadFile,request:Request):

    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400,detail="File not supported .File should be in .csv format")
    input_file_path = os.path.join(UPLOAD_PATH,f'{uuid.uuid4()}_{file.filename}')

    with open(file=input_file_path,mode='wb') as file_obj:
        file_obj.write(await file.read())

    df = pd.read_csv(input_file_path)
    df['Processed'] = "Yes"
    output_file_name = f'output_{uuid.uuid4()}_{file.filename}'
    output_file_path = os.path.join(UPLOAD_PATH, output_file_name)
    df.to_csv(output_file_path, index=False)

    base_url = f"{request.url.scheme}://{request.client.host}:{request.url.port}"

    return JSONResponse(
        content={"message": "File processed successfully", "download_url": f"{base_url}/download/{output_file_name}"}
    )


@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = os.path.join(UPLOAD_PATH, file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")

    # Return the file as a response
    return FileResponse(file_path, filename=file_name)
