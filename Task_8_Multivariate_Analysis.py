# ============================================================
# Task 8 : Multivariate Analysis
# Credit Card Approval Prediction System
# ============================================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# Read Dataset
# ------------------------------------------------------------

app = pd.read_csv("Dataset/application_record.csv")

# ------------------------------------------------------------
# Select Numerical Columns
# ------------------------------------------------------------

numerical_data = app.select_dtypes(include=['int64', 'float64'])

# ------------------------------------------------------------
# Correlation Matrix
# ------------------------------------------------------------

correlation_matrix = numerical_data.corr()

print("\nCorrelation Matrix:\n")
print(correlation_matrix)

# ------------------------------------------------------------
# Heatmap
# ------------------------------------------------------------

plt.figure(figsize=(12,8))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nTask 8 Completed Successfully!")
