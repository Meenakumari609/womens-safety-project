import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('survey_data_500.csv')

print(df.head())

feel_safe_counts = df['Feel Safe'].value_counts()
print("\nFeel Safe Counts:")
print(feel_safe_counts)

feel_safe_counts.plot(kind='bar', color=['red', 'orange', 'green'])
plt.title('How Safe Do Women Feel?')
plt.xlabel('Feel Safe')
plt.ylabel('Number of Respondents')
plt.show()
