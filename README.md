# DiaPredict AI

A Flask web application that uses a trained machine-learning model to estimate diabetes risk from basic health information. The app displays a predicted status, probability score, BMI category, and age on a results page.

> **Medical disclaimer:** This application provides an experimental machine-learning estimate and is not a medical diagnosis. Do not use it as a substitute for advice from a qualified healthcare professional.

## Features

- Web-based diabetes-risk prediction form
- BMI calculator in the dashboard
- Prediction result with risk probability and health metrics
- Docker and Docker Compose support
- Vercel deployment support

## Project Structure

```text
.
├── app.py                 # Flask application and prediction route
├── model.py               # Model-training and evaluation workflow
├── modelD.pkl             # Trained model
├── scalerD.pkl            # Fitted feature scaler
├── requirements.txt       # Python dependencies
├── dockerfile             # Docker image definition
├── docker-compose.yml     # Docker Compose configuration
├── templates/
│   ├── index.html         # Input dashboard
│   └── result.html        # Prediction results page
├── static/
│   └── style.css          # Application styles
└── VERCEL_DEPLOYMENT.md   # Detailed Vercel instructions
```

## Requirements

- Python 3.11 or later
- The root-level files `modelD.pkl` and `scalerD.pkl`


## Input Features

The prediction endpoint receives these form fields:

| Field | Description |
| --- | --- |
| `Age` | Patient age |
| `BMI` | Body mass index |
| `Gender` | `1` for male, `0` for female |
| `Physical_Activity` | `1` for yes, `0` for no |
| `Smoked` | `1` for yes, `0` for no |
| `HighBP` | `1` for yes, `0` for no |
| `GeneralHealth` | `Poor`, `Fair`, `Good`, or `VeryGood` |

The feature order sent to the scaler and model is defined in `app.py` and must stay consistent with the order used during training.

## Model Workflow

`model.py` contains the exploratory analysis, preprocessing, model training, and evaluation workflow. It trains and compares logistic regression, decision tree, random forest, and MLP classifiers using the BRFSS dataset.

The deployed Flask app does not train a model at startup. It loads the pre-trained `modelD.pkl` and `scalerD.pkl` files, so both files must be available in the project root.



