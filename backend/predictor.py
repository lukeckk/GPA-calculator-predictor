import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import seaborn as sns
import numpy as np

df = pd.read_csv("dataset/gpa.csv")

X = df[['study_hours', 'work_hours', 'sleep_hours', 'interest']]
y = df['GPA']

# Feature engineering
X['study_interest'] = X['study_hours'] * X['interest']

# Log transformation to handle non-linearity
X['work_hours'] = np.log1p(X['work_hours'])  

# Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Polynomial features (degree=2)
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X_scaled)

predict_model = LinearRegression()
predict_model.fit(X_poly, y)

coefficients = predict_model.coef_
intercept = predict_model.intercept_

# print("Intercept (β0):", intercept)
# print("Coefficients:")
# for i, coef in enumerate(coefficients):
#     print(f"β{i+1}: {coef}")

def predict_gpa(study_hours, work_hours, sleep_hours, interest):
    input_df = pd.DataFrame([[study_hours, np.log1p(work_hours), sleep_hours, interest, study_hours * interest]],
                            columns=['study_hours', 'work_hours', 'sleep_hours', 'interest', 'study_interest'])

    input_scaled = scaler.transform(input_df)

    input_poly = poly.transform(input_scaled)

    predicted_gpa = predict_model.predict(input_poly)[0]

    return round(predicted_gpa, 2) 

# Example Prediction
# predicted_gpa = predict_gpa(12, 0, 10, 10)
# print(f"Predicted GPA: {predicted_gpa:.2f}")
