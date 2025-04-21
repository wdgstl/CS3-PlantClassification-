from pathlib import Path
from describe_plant import get_description
from classifier import * 
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
import uuid
import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

#TODO Modify these 2 lines to fit your new model
model = classifier(custom_train_job = True, model_type= "your_torchvision_model")
model.fine_tune(path_to_training_data="path", path_to_validation_data = "path")

#TODO Modify this line to point to then folder holding the test parquets 
preds = model.predict(image_path="path_to_test_set")
print(preds)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    temp_dir = Path("temp_uploads")
    temp_dir.mkdir(exist_ok=True)
    temp_file_path = temp_dir / f"{uuid.uuid4()}_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        results = model.predict(str(temp_file_path))
        os.remove(temp_file_path)
        return {"prediction": results}
    except Exception as e:
        os.remove(temp_file_path)
        return {"error": str(e)}

@app.get("/describe")
async def describe(plant_name):
    if OPENAI_API_KEY:
        description = get_description(plant_name=plant_name, OPENAI_KEY=OPENAI_API_KEY)
    else:
        description = "Add OpenAI API Key to get description and edibility of plant"
    return {"message": description}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)