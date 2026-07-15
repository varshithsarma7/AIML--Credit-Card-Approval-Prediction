# 💳 Credit Card Approval Prediction System

## 📌 Project Overview

The **Credit Card Approval Prediction System** is a Machine Learning-based application developed to predict whether a customer's credit card application is likely to be **Approved** or **Rejected** based on applicant information.

The project follows a complete Machine Learning pipeline, including data collection, preprocessing, exploratory data analysis, feature engineering, model building, evaluation, and deployment using the Flask framework.

---

# 👥 Team Members

| Name | Email | Role |
|------|-------|------|
| **Varshith Sarma** | varshithsarmasalagrama@gmail.com | Team Lead |
| Srinivasu Pakkurthi | vasu72424@gmail.com | Member |
| Mathurthi Satya Santosh | satyasantoshmathurthi@gmail.com | Member |
| Khaja Karimulla Mohammed | mdkkarimulla786@gmail.com | Member |
| Sidhardha S | ssidhardha1@gmail.com | Member |

---

# Dataset

The dataset is not included in this repository because of GitHub file size limitations.

Download the dataset from:
https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction

Place the following files inside a folder named `Dataset` before running the project:

- application_record.csv
- credit_record.csv

Contains applicant details such as:

- Applicant ID
- Gender
- Car Ownership
- Property Ownership
- Number of Children
- Annual Income
- Income Type
- Education Level
- Family Status
- Housing Type
- Age
- Employment Details
- Mobile Phone
- Work Phone
- Email
- Occupation Type
- Family Members

### 2. credit_record.csv

Contains customer credit history including:

- Applicant ID
- Monthly Credit Record
- Credit Status

The datasets are merged using the **ID** column for further preprocessing and model training.

> **Note:**  
> Due to GitHub file size limitations, the dataset files are not included in this repository.

Dataset Source:
https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask

---

# 📁 Repository Structure

```
AIML--Credit-Card-Approval-Prediction/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
│
├── Task_01_Entity_Relationship_Diagram.pdf
├── Task_02_Link.md
├── Task_03_Work_Flow.md
├── Task_04_Download_Dataset.md
├── Task_05_Importing_Libraries.py
├── Task_06_Read_Dataset.py
├── Task_07_Univariate_Analysis.py
├── Task_08_Multivariate_Analysis.py
├── Task_09_Descriptive_Analysis.py
├── Task_10_Drop_Duplicate_Features.py
├── Task_11_Handling_Missing_Values.py
├── Task_12_Data_Cleaning_and_Merging.py
├── Task_13_Feature_Engineering.py
├── Task_14_Handling_Categorical_Values.py
├── Task_15_Logistic_Regression_Model.py
├── Task_16_Random_Forest_Model.py
├── Task_17_Decision_Tree_Model.py
├── Task_18_Building_HTML_Pages.html
├── Task_19_Build_Python_Script.py
├── Task_20_Run_Application.md
└── Task_21_Conclusion.md
```

---

# 🤖 Machine Learning Models Used

- Logistic Regression
- Decision Tree
- Random Forest

Among all the models, the **Random Forest Classifier** produced the best prediction performance.

---

# 🚀 How to Run the Project

## Step 1

Clone the repository.

```bash
git clone https://github.com/varshithsarma7/AIML--Credit-Card-Approval-Prediction.git
```

## Step 2

Install the required packages.

```bash
pip install -r requirements.txt
```

## Step 3

Download the dataset and place the following files inside a folder named **Dataset**.

```
Dataset/
│
├── application_record.csv
└── credit_record.csv
```

## Step 4

Run the Flask application.

```bash
python app.py
```

## Step 5

Open your browser.

```
http://127.0.0.1:5000/
```

Enter the applicant details and click **Predict** to view the credit card approval prediction.

---

# 🎯 Project Workflow

1. Download Dataset
2. Import Libraries
3. Read Dataset
4. Exploratory Data Analysis
5. Data Cleaning
6. Handling Missing Values
7. Feature Engineering
8. Handling Categorical Values
9. Train Machine Learning Models
10. Compare Model Performance
11. Deploy using Flask
12. Predict Credit Card Approval

---

# 📄 License

This project is intended for educational and internship purposes.

---

## ⭐ Team

Developed as part of the **APSCHE AI & ML Virtual Internship** by **Team Credit Card Approval Prediction**.
