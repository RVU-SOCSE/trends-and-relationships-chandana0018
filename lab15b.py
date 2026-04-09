import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:/Users/keert/OneDrive/Documents/lab13.csv")
plt.scatter(df['YearsExperience'], df['Salary'])
plt.ylabel('Salary')
plt.xlabel('YearsExperience')
plt.legend()
plt.show()
sns.scatterplot(x = df['Salary'], y = df['YearsExperience'])
plt.show()

