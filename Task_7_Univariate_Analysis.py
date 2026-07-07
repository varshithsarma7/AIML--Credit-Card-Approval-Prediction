# ============================================================
# Task 7 : Univariate Analysis
# Credit Card Approval Prediction System
# ============================================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Dataset
app = pd.read_csv("Dataset/application_record.csv")

# Set Plot Style
sns.set(style="whitegrid")

# ============================================================
# OCCUPATION TYPE
# ============================================================

print("\nNumber of Applicants by Occupation:\n")
print(app["OCCUPATION_TYPE"].value_counts())

plt.figure(figsize=(15,6))

sns.countplot(
    x="OCCUPATION_TYPE",
    data=app,
    order=app["OCCUPATION_TYPE"].value_counts().index,
    palette="Set2"
)

plt.title("Occupation Type Distribution")
plt.xlabel("Occupation Type")
plt.ylabel("Count")
plt.xticks(rotation=60)

plt.tight_layout()
plt.savefig("Graphs/Occupation_Type_Countplot.png")
plt.show()

# ============================================================
# INCOME TYPE
# ============================================================

print("\nIncome Type Distribution:\n")
print(app["NAME_INCOME_TYPE"].value_counts())

plt.figure(figsize=(10,6))

sns.countplot(
    x="NAME_INCOME_TYPE",
    data=app,
    order=app["NAME_INCOME_TYPE"].value_counts().index,
    palette="viridis"
)

plt.title("Income Type Distribution")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("Graphs/Income_Type_Countplot.png")
plt.show()

# ============================================================
# EDUCATION TYPE
# ============================================================

print("\nEducation Level Distribution:\n")
print(app["NAME_EDUCATION_TYPE"].value_counts())

plt.figure(figsize=(10,6))

sns.countplot(
    x="NAME_EDUCATION_TYPE",
    data=app,
    order=app["NAME_EDUCATION_TYPE"].value_counts().index,
    palette="coolwarm"
)

plt.title("Education Level Distribution")
plt.xticks(rotation=25)

plt.tight_layout()
plt.savefig("Graphs/Education_Countplot.png")
plt.show()

print("\nTask 7 Completed Successfully!")
