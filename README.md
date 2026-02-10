# Car Price Prediction 

## Overview

The **Car Price Prediction** project is a machine learning application that predicts the selling price of a used car based on various features such as brand, model year, fuel type, transmission, mileage, engine capacity, and ownership details. This project demonstrates the complete data science workflow, from data preprocessing and exploratory data analysis (EDA) to model building, evaluation, and deployment using a web interface.

## Objectives

* To analyze car-related data and identify key factors affecting car prices
* To perform data cleaning, preprocessing, and feature engineering
* To build and evaluate machine learning regression models
* To deploy the trained model using a web framework (Flask)
* To provide real-time car price predictions through a user-friendly interface

## Machine Learning Problem Type

* **Problem Type:** Supervised Learning
* **Task:** Regression
* **Target Variable:** Car Price

## Dataset Description

The dataset contains information related to used cars. It is a real-world style dataset collected from open car listing sources.

### Key Features:

* Car Name / Brand
* Year of Manufacture
* Fuel Type (Petrol, Diesel, CNG, etc.)
* Engine Capacity (CC)
* Ownership Type
* Kilometers Driven

## Exploratory Data Analysis (EDA)

EDA was performed to understand data patterns and relationships.

### EDA Techniques Used:

* Descriptive statistics
* Handling missing values
* Outlier detection using box plots
* Distribution analysis using histograms
* Correlation analysis
* Feature importance analysis

## Technologies & Tools Used

### Programming & Libraries

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

### Web & Deployment

* Flask
* HTML
* CSS

## Data Preprocessing

* Handling missing values
* Encoding categorical variables 
* Feature scaling 
* Removing irrelevant columns
* Train-test split

## Machine Learning Models Used

* Linear Regression

## Model Evaluation Metrics

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

## Web Application

A Flask-based web application was developed where users can:

* Enter car details
* Submit the form
* Get an estimated car price instantly

## Car Price Prediction Web Application GIF

<img src="https://github.com/Nivethanajacob/carprice_flask/blob/main/static/image/GIF-ezgif.com-video-to-gif-converter.gif">

## How to Run the Project

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project directory

```bash
cd car_price_prediction
```

3. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate    
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run the Flask application

```bash
python app.py
```

6. Open browser and visit

```
http://127.0.0.1:5000/
```
## Output 

Model Deployment (Flask App):https://carpricepredict-flask.onrender.com

## Results

* Achieved accurate car price predictions
* Identified important features affecting car prices
* Successfully deployed ML model as a web application

