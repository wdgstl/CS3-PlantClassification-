# CS3 Case Study: Fine-Tune a Torchvision Model for Plant Classification

![image](https://github.com/user-attachments/assets/6ff95681-4495-45b9-a9af-dbf04bb13490)

## Repo Format

## Setup
- create venv: python3 -m venv myvenv
- activate venv: source myvenv/bin/activate
- install dependencies: pip3 install - requirements.txt

## Steps
1. Review [past model performance](https://github.com/wdgstl/CS3-PlantClassification-/blob/main/output/model_comparison.png)
2. Research other torchvision model architectures, and select [one](https://pytorch.org/vision/0.9/models.html)
3. Review the steps in [fine tuning](https://dev.to/santoshpremi/fine-tuning-a-pre-trained-model-in-pytorch-a-step-by-step-guide-for-beginners-4p6l) a torchvision model
4. Load the training and validaton data from [Pl@ntNet-300K](https://zenodo.org/records/4726653#.YhNbAOjMJPY) Hint: you may find it easier and more efficient to load the data in parquet form - it has been repackaged [here](https://huggingface.co/datasets/mikehemberger/plantnet300K/tree/main/data). You should save the data in the [data folder](https://github.com/wdgstl/CS3-PlantClassification-/tree/main/data)
5. Complete TODOs in [classisifer.py](https://github.com/wdgstl/CS3-PlantClassification-/blob/main/scripts/classifier.py)
   - update __init__ function to initialize model according to model documentation
   - update the fine_tune function to update the weights of self.model
   - update the preprocess_data function inside of fine_tune to process training and validation data
6. Load the testing data (in parquet form), from [here](https://huggingface.co/datasets/mikehemberger/plantnet300K/tree/main/data). You should save the data in the [data folder](https://github.com/wdgstl/CS3-PlantClassification-/tree/main/data)
7. Complete TODOs in [main.py](https://github.com/wdgstl/CS3-PlantClassification-/blob/main/scripts/main.py)
   - update the lines to initialize the classifier model
   - uppdate the lines to predict using your new model
8. Run [main.py](https://github.com/wdgstl/CS3-PlantClassification-/blob/main/scripts/main.py) to get: your fine-tuned models evaluation metrics and an exposed FastAPI that allows you to: 1. predict the species of a plant given an image file, 2. predict the edibiity of a plant given its name.
9. Reflect on your model performance by answering these questions in [reflection.txt](https://github.com/wdgstl/CS3-PlantClassification-/blob/main/output/reflection.txt). Did you outpeform the past models? Which ones did your model perform better on worse than? Why are you seeing these results? Reflect on the differences in architecture among your custom model and the other models.  

## Optional 
To use the edibility classification feature of this tool, you must have an OpenAI API key. To use this feature, create a .env file inside of the scripts directory, and simple set: OPENAI_KEY = "YOUR_KEY".
