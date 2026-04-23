🎓 Predicting First-Year Academic Performance

📌 Overview
This project uses Multiple Linear Regression to analyze and predict first-year university performance based on student data.

The goal is to understand:

What factors actually influence student success
Which variables matter the most
How well we can predict performance using data

🎯 Objectives

Apply Multiple Linear Regression to predict student performance
Identify key predictors (HS_GWA, Admission Score, Course, Strand)
Evaluate model performance using R², Adjusted R², and ANOVA
Interpret how each variable affects academic outcomes

🧹 Data Preparation

Missing numerical values handled using median imputation
Missing categorical values replaced with "Unknown"
No duplicate or inconsistent data found
Data prepared for regression modeling

📊 Exploratory Data Analysis (EDA)

🔹 Correlation Analysis (Multicollinearity Check)



Strong relationship between HS_GWA and First-Year GWA
Moderate relationship between Admission Score and performance
Weak relationship between Gender and performance
No serious multicollinearity issues

🔹 Strand vs First-Year Performance



STEM students perform the best
TVL students show lower performance
Academic background clearly affects results

🧠 Model Building

📌 Features Used:

HS_GWA
Admission Score
Course (dummy variables)
Strand (dummy variables)

❌ Excluded:

Gender
School Type

Reason: Weak relationship + potential noise

📈 Model Performance

R² = 0.398
Adjusted R² = 0.323
MSE = 32.02
F-statistic = 30.39 (p < 0.001)

👉 The model explains about 40% of student performance

🔍 Key Insights

HS_GWA is the strongest predictor
Admission Score matters, but less than HS_GWA
Course and Strand influence performance
Gender and School Type have little impact

⚠️ Limitations

Model explains only ~40% → other factors missing
Possible missing variables:
Study habits
Attendance
Motivation
Socio-economic factors

💡 Recommendations

Focus on high school performance during admissions
Provide support for:
TVL students
Lower-performing courses
Implement early intervention systems
Collect more student behavior data

🛠️ Technologies Used
Python and Excel
Pandas
Matplotlib / Seaborn
Statistical Modeling

📌 Conclusion
This project shows that past academic performance is the strongest indicator of future success.
While the model is useful, student performance is influenced by many other factors beyond academics.

👥 Contributors
Katlego Mmako
Tebogo Nyamane
Lesego Lekoane
Lehlogonolo Mothibi
Jesicca Ngobeni

