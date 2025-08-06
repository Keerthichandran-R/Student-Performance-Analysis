
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("student_scores.csv")

# Display first few records
print("Sample Data:")
print(df.head())

# Calculate average scores
print("\nAverage Scores:")
print(df[['Math', 'Science', 'English']].mean())

# Top performer in each subject
print("\nTop Performers:")
for subject in ['Math', 'Science', 'English']:
    top_student = df.loc[df[subject].idxmax()]
    print(f"{subject}: {top_student['Name']} ({top_student[subject]})")

# Optional: Class-wise average scores
class_avg = df.groupby("Class")[['Math', 'Science', 'English']].mean()
print("\nClass-wise Average Scores:")
print(class_avg)

# Plot class-wise average
class_avg.plot(kind='bar', title='Class-wise Average Scores')
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
