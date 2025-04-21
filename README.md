# CS3 Case Study: Fine-Tune a Torchvision Model for Plant Classification

![image](https://github.com/user-attachments/assets/6ff95681-4495-45b9-a9af-dbf04bb13490)

## Repo Format

## Setup
- create venv: python3 -m venv myvenv
- activate venv: source myvenv/bin/activate
- install dependencies: pip3 install - requirements.txt

## Steps
1. Review ([past model performance](https://github.com/wdgstl/CS3-PlantClassification-/blob/main/output/model_comparison.png) )
2. Research other torchvision model architectures, and select ([one](https://pytorch.org/vision/0.9/models.html))
4. Review the steps in ([fine tuning](https://dev.to/santoshpremi/fine-tuning-a-pre-trained-model-in-pytorch-a-step-by-step-guide-for-beginners-4p6l)) a torchvision model
5. Complete TODOs in classisifer.py
   - update __init__.py to initialize model according to model documentation
   - update fine_tune.py to update the weights of self.model
   - update preprocess_data.py inside of fine_tune.py to process training and validation data 
3. Complete TODOs in main.py
   - update the lines to initialize the classifier model
   - uppdate the lines to predict using your new model
5. Run main.py to get: your fine-tuned models evaluation metrics and an exposed FastAPI that allows you to: 1. predict the species of a plant given an image file, 2. predict the edibiity of a plant given its name. 

## Optional 
To use the edibility classification feature of this tool, you must have an OpenAI API key. To use this feature, create a .env file inside of the scripts directory, and simple set: OPENAI_KEY = "YOUR_KEY".
