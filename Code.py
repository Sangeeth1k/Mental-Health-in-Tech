# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset (replace with your dataset path or URL)
# data = pd.read_csv("mental_health_survey.csv") # Original line

# Create a mock dataset based on the description
data = pd.DataFrame({
    'Gender': np.random.choice(['Male', 'Female', 'Non-binary'], 100),
    'Have you sought treatment?': np.random.choice(['Yes', 'No'], 100),
    'Does your employer provide mental health support?': np.random.choice(['Yes', 'No', 'Don\'t know'], 100),
    # Add other relevant columns if needed for a more complete analysis
})


# -------------------------------
# 1. Pie Chart: Gender split
# -------------------------------
gender_counts = data['Gender'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Gender Distribution of Tech Professionals")
plt.show()

# -------------------------------
# 2. Bar Chart: Anxiety rates by Gender
# -------------------------------
plt.figure(figsize=(7,5))
sns.countplot(x="Gender", hue="Have you sought treatment?", data=data, palette="Set2")
plt.title("Anxiety / Treatment Seeking by Gender")
plt.ylabel("Number of Professionals")
plt.show()

# -------------------------------
# 3. Heatmap: Workplace Support vs Anxiety Levels
# -------------------------------
cross_tab = pd.crosstab(data['Does your employer provide mental health support?'],
                        data['Have you sought treatment?'])

plt.figure(figsize=(7,5))
sns.heatmap(cross_tab, annot=True, fmt="d", cmap="coolwarm")
plt.title("Workplace Support vs Anxiety / Treatment")
plt.show()
