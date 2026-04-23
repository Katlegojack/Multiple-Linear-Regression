import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("student_performance_data.xlsx")

# Basic check
print(df.head())
print(df.info())

# Course
print("\nCourse Distribution:")
print(df["Course"].value_counts())
print(df["Course"].value_counts(normalize=True) * 100)

# Strand
print("\nStrand Distribution:")
print(df["Strand"].value_counts())
print(df["Strand"].value_counts(normalize=True) * 100)

# Numerical Summary
print("\nNumerical Summary:")
print(df[["HS_GWA", "Admission_Score", "First_Year_GWA"]].describe())

# Correlation
print("\nCorrelation Matrix:")
corr_matrix = df[["HS_GWA", "Admission_Score", "First_Year_GWA"]].corr()
print(corr_matrix)

# Course vs Performance
print("\nCourse vs First Year GWA:")
print(df.groupby("Course")["First_Year_GWA"].mean())

# Strand vs Performance
print("\nStrand vs First Year GWA:")
print(df.groupby("Strand")["First_Year_GWA"].mean())

# Trend Analysis
df["HS_GWA_Group"] = pd.cut(df["HS_GWA"], bins=5)
print("\nHS_GWA Trend:")
print(df.groupby("HS_GWA_Group")["First_Year_GWA"].mean())

df["Admission_Group"] = pd.cut(df["Admission_Score"], bins=5)
print("\nAdmission Score Trend:")
print(df.groupby("Admission_Group")["First_Year_GWA"].mean())

# Summary Statistics
print("\nSummary Statistics:")

summary = df[["HS_GWA", "Admission_Score", "First_Year_GWA"]].describe()

print(summary)

# Visualization
sns.heatmap(corr_matrix, annot=True)
plt.title("Correlation Matrix")
plt.show()

sns.boxplot(x="Course", y="First_Year_GWA", data=df)
plt.title("Course vs First Year GWA")
plt.show()

sns.boxplot(x="Strand", y="First_Year_GWA", data=df)
plt.title("Strand vs First Year GWA")
plt.show()