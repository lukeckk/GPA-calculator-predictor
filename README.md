## GPA Calculator & Predictor

### Demo link: 
https://gpa-calculator-tj9p.onrender.com/

This project does the following:
1. Calculates the GPA a student needs to achieve with their remaining credits to reach their target GPA
2. Predicts student GPA based on study habits, sleep, work hours, and interest. It uses feature engineering to improve predictions

This project acheives the following:
1. Reduces manual calculation and error
2. Allows student to estimate gpa according to their lifestyle and plan accordingly to achieve better time management and academic result

### Dataset and Feature Engineering
A custom dataset containing study hours, work hours, sleep hours, and interest levels was used to train a linear regression model. Feature engineering was applied to enhance the model:

- **Interaction Feature**: `study_hours * interest`
- **Log Transformation**: Applied to `work_hours`
- **Polynomial Features**: Used to capture non-linear relationships

#### Feature Correlation
![Feature Correlation](static/images/heatmap.png)

#### Data Distribution
![Pairplot](static/images/pairplot.png)

#### Model Performance
- **Mean Absolute Error (MAE)**: 0.0706
- **R² Score**: 0.9935


