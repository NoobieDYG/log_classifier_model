# Log Classification Project

This project classifies logs using BERT, LLM, and regex classification.

## Project Structure

- **models/**: Contains the exported logistic regression joblib file.
- **resources/**: Contains the test and output CSV files.
- **training/**: Contains the Jupyter notebook (`.ipynb`) file in which we analyzed and cleaned data.
- **dataset/**: Contains the sample dataset.

## Classifier Models

Each classifier model is in its own file. All models are imported into the `classify.py` file, which then predicts the log messages.

## Frontend

A simple frontend using FastAPI is still to be made.

## Note

This project is not an original idea and was made by following a tutorial.