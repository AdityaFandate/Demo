import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("employee_salary_dataset.csv")
print(df.describe())
df.hist(figsize=(10, 6))
plt.tight_layout()
plt.show()
corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()