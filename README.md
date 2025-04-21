## CS3 Case Study: Fine-Tune a Torchvision Model for Plant Classification



<img width="19" alt="image" src="https://github.com/user-attachments/assets/f57ea81a-3400-4907-874c-19a77b6d38ae" />



# Setup
- create venv: python3 -m venv myvenv
- activate venv: source myvenv/bin/activate
- install dependencies: pip3 install - requirements.txt

# Steps
1. Research and select model (visit )
2. Complete TODOs in classisifer.py
   - update __init__.py to initialize model according to torchvision models documentation
   - update fine_tune.py to update the weights of self.model
   - update preprocess_data.py inside of fine_tune.py to process training and validation data 
3. Complete TODOs in main.py
4. Run main.py to get: your fine-tuned models evaluation metrics and an exposed FastAPI that allows you to: 1. predict the species of a plant given an image file, 2. predict the edibiity of a plant given its name. 

## Optional 
To use the edibility classification feature of this tool, you must have an OpenAI API key. To use this feature, create a .env file inside of the scripts directory, and simple set: OPENAI_KEY = "YOUR_KEY".
