# ============================================================
# Task 9 : Descriptive Analysis
# Credit Card Approval Prediction System
# ============================================================

# Import Libraries
import pandas as pd

# ------------------------------------------------------------
# Read Dataset
# ------------------------------------------------------------

app = pd.read_csv("Dataset/application_record.csv")

# ------------------------------------------------------------
# Basic Information
# ------------------------------------------------------------

print("\n========== Dataset Shape ==========")
print(app.shape)

print("\n========== Dataset Columns ==========")
print(app.columns)

print("\n========== Dataset Information ==========")
app.info()

# ------------------------------------------------------------
# Descriptive Statistics
# ------------------------------------------------------------

print("\n========== Numerical Statistics ==========")
print(app.describe())

print("\n========== Categorical Statistics ==========")
print(app.describe(include='object'))

# ------------------------------------------------------------
# Unique Values
# ------------------------------------------------------------

print("\n========== Unique Values ==========")
print(app.nunique())

print("\nTask 9 Completed Successfully!")
