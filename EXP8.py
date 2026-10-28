# Experiment No. 08: Linear Regression with Model Diagnostics

import pandas as pd
# pyrefly: ignore[missing-import]
import numpy as np
# pyrefly: ignore[missing-import]
import matplotlib.pyplot as plt
import seaborn as sns
# pyrefly: ignore[missing-import]
import statsmodels.api as sm

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
# pyrefly: ignore[missing-import]
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 1. Create Car Sales Dataset
data = {
    'Engine_Size': [1.2, 1.5, 1.8, 2.0, 1.4,
                    2.2, 1.6, 2.5, 1.3, 1.9,
                    2.1, 1.7, 2.4, 1.5, 2.8],

    'Mileage': [22, 20, 18, 16, 21,
                14, 19, 12, 22, 17,
                15, 18, 13, 20, 10],

    'Age': [2, 3, 2, 4, 1,
            5, 3, 6, 2, 4,
            5, 3, 6, 2, 8],

    'Price': [6.5, 8.0, 10.5, 12.0, 7.5,
              14.0, 9.0, 16.5, 7.0, 11.0,
              13.5, 9.5, 15.5, 8.5, 18.0]
}

df = pd.DataFrame(data)

print("CAR SALES DATASET")
print(df.to_string(index=False))

# 2. Define Independent and Dependent Variables
X = df[['Engine_Size', 'Mileage', 'Age']]
y = df['Price']

# 3. Fit Linear Regression Model
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("\nLINEAR REGRESSION MODEL")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# 4. Evaluate the Model
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)

print("\nMODEL EVALUATION")
print("R2 Score:", r2)
print("MSE:", mse)
print("RMSE:", rmse)

# 5. Calculate VIF
X_vif = sm.add_constant(X)

vif = pd.DataFrame()
vif['Variable'] = X_vif.columns
vif['VIF'] = [
    variance_inflation_factor(X_vif.values, i)
    for i in range(X_vif.shape[1])
]

print("\nVIF RESULTS")
print(vif.to_string(index=False))

# 6. Calculate Residuals
residuals = y - y_pred

diagnostics = pd.DataFrame({
    'Actual': y,
    'Predicted': y_pred,
    'Residual': residuals
})

print("\nRESIDUALS")
print(diagnostics.round(3).to_string(index=False))

# 7. Plot Residuals vs Fitted Values
plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("Fitted / Predicted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs Fitted Values")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 8. Fit OLS Model for Statistical Diagnostics
X_sm = sm.add_constant(X)
ols_model = sm.OLS(y, X_sm).fit()

print("\nOLS REGRESSION SUMMARY")
print(ols_model.summary())

# 9. Calculate Cook's Distance
influence = ols_model.get_influence()
cooks_distance = influence.cooks_distance[0]

diagnostics['Cook_Distance'] = cooks_distance

print("\nCOOK'S DISTANCE")
print(np.round(cooks_distance, 4))

# 10. Plot Cook's Distance
plt.figure(figsize=(10, 5))
plt.stem(
    range(1, len(cooks_distance) + 1),
    cooks_distance
)
plt.axhline(
    y=4 / len(df),
    color='red',
    linestyle='--',
    label='Threshold = 4/n'
)
plt.xlabel("Observation Number")
plt.ylabel("Cook's Distance")
plt.title("Cook's Distance Plot")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 11. Identify Influential Observations
n = len(df)
threshold = 4 / n

diagnostics['Influential'] = (
    diagnostics['Cook_Distance'] > threshold
)

print("\nCOOK'S DISTANCE THRESHOLD:", round(threshold, 4))

print("\nCOMPLETE DIAGNOSTIC RESULTS")
print(diagnostics.round(4).to_string(index=True))

print("\nINFLUENTIAL OBSERVATIONS")
found = False

for i in range(n):
    if cooks_distance[i] > threshold:
        print(
            "Observation:", i + 1,
            "| Cook's Distance:", round(cooks_distance[i], 4)
        )
        found = True

if not found:
    print("No observations exceed the screening threshold.")

# 12. Conclusion
print("\nCONCLUSION")
print("Linear regression was performed successfully.")
print("VIF, residual plots, and Cook's distance were used")
print("to evaluate multicollinearity, residual patterns,")
print("and influential observations.")