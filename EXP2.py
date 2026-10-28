import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("employee_salary_dataset.csv")

print("===== ORIGINAL DATA =====")
print(df)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# 1. Handle missing numeric values
numeric_cols = ["Age", "Monthly_Salary", "Performance_Score"]

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# 2. Handle missing categorical values
categorical_cols = ["Department"]

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\n===== AFTER HANDLING MISSING VALUES =====")
print(df)

# 3. Encoding (One-Hot Encoding)
df = pd.get_dummies(
    df,
    columns=["Department"],
    dtype=float
)

print("\n===== AFTER ENCODING =====")
print(df)

# 4. Scaling
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("\n===== AFTER SCALING =====")
print(df)

# 5. Outlier Detection using IQR
Q1 = df[numeric_cols].quantile(0.25)
Q3 = df[numeric_cols].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = (
    (df[numeric_cols] < lower_limit) |
    (df[numeric_cols] > upper_limit)
)

print("\n===== OUTLIERS DETECTED =====")
print(outliers)

print("\n===== OUTLIER COUNTS =====")
print(outliers.sum())

print("\n===== FINAL DATA INFO =====")
df.info()
