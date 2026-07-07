# ============================================================
# Task 5 : Importing the Libraries
# Credit Card Approval Prediction System
# ============================================================

# Data Manipulation Libraries
import pandas as pd
import numpy as np

# Data Visualization Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Machine Learning Algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# XGBoost Classifier
from xgboost import XGBClassifier

# Flask Libraries
from flask import Flask, render_template, request

# Model Saving
import joblib

print("=" * 60)
print("All Required Libraries Imported Successfully!")
print("=" * 60)
