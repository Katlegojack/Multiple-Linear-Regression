import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import statsmodels.api as sm

# LOAD DATA
df = pd.read_excel("student_performance_data.xlsx")


# ENCODING
df_encoded = pd.get_dummies(df, columns=['Course', 'Strand'], drop_first=True)

# DEFINE independent and dependent variables  
X = df_encoded.drop("First_Year_GWA", axis=1)
y = df_encoded["First_Year_GWA"]


# FEATURE ENGINEERING
#X["HS_Admission"] = X["HS_GWA"] * X["Admission_Score"]
#X["HS_GWA_squared"] = X["HS_GWA"] ** 2


# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TRAIN MODEL
model = LinearRegression()
model.fit(X_train, y_train)

# PREDICTIONS
y_pred = model.predict(X_test)

# STEP 5: VALIDATION

# R² and Adjusted R²
r2 = r2_score(y_test, y_pred)

n = len(y_test)          # number of observations
p = X_test.shape[1]      # number of predictors

adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2)
print("Adjusted R2:", adjusted_r2)

# ANOVA (F-test) 
X_train_sm = sm.add_constant(X_train)

X_train_sm = X_train_sm.astype(float)
y_train_sm = y_train.astype(float)

model_sm = sm.OLS(y_train_sm, X_train_sm).fit()

print("\nANOVA / F-test Results:")
print(model_sm.summary())

# COEFFICIENTS
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\nFeature Importance:")
print(coefficients)
