from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from faker import Faker
import csv
import json
import io
from typing import Dict,List
from src.main import DataGenerator

app = FastAPI()
fake = Faker()
templates = Jinja2Templates(directory="../templates")

# This will be used to generate mock data based on the user's fields
class Field(BaseModel):
    name: str
    data_type: str

@app.get("/",response_class=HTMLResponse)
async def get_form(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/generate/")
async def generate_data(field_dict: str = Form(...), num_records: int = Form(...)):
    # Parse the incoming JSON string to a Python object
    fields_list = json.loads(field_dict)

    # Initialize the DataGenerator (or your actual class for mock data generation)
    generator = DataGenerator()
    
    # Translate the fields using your logic
    translated_fields = generator.translate(data_dict=fields_list)

    # Generate the mock data
    data = generator.generate(translated_fields, num_records)
    # Return the generated data as JSON
    return data

@app.get("/download")
async def download_data():
    # Generate mock data to download
    data = [{"name": fake.name(), "email": fake.email()} for _ in range(10)]  # Replace with actual generated data
    
    # Create a CSV in-memory file
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    
    output.seek(0)
    return FileResponse(output, media_type="text/csv", filename="mock_data.csv")
