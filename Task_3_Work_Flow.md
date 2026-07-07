# Work Flow

The Credit Card Approval Prediction System follows the workflow below:

## Step 1: Dataset Collection
- Download the `application_record.csv` and `credit_record.csv` datasets.
- Store them in the Dataset folder.

## Step 2: Import Required Libraries
- Import NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, Flask, and XGBoost.

## Step 3: Read the Dataset
- Load both datasets using Pandas.
- Display the first few records and examine the dataset structure.

## Step 4: Data Preprocessing
- Handle missing values.
- Remove duplicate records.
- Merge both datasets using the `ID` column.
- Encode categorical variables.
- Perform feature engineering.

## Step 5: Exploratory Data Analysis
- Perform descriptive analysis.
- Perform univariate analysis.
- Perform multivariate analysis.

## Step 6: Model Building
Train multiple machine learning models:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

## Step 7: Model Evaluation
Evaluate the models using:
- Accuracy Score
- Confusion Matrix
- Classification Report

Select the best-performing model.

## Step 8: Web Application Development
Develop a Flask web application with:
- Home Page
- Prediction Form
- Prediction Result Page

## Step 9: Prediction
- The user enters applicant details.
- The trained model predicts whether the credit card application is **Approved** or **Rejected**.

## Step 10: Deployment
- Run the Flask application locally.
- Test the application.
- Upload the completed project to GitHub.
