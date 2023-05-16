import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv('data/employ.csv') #Load your csv file

#Load your coulmns
column1 = df['Male']
column2 = df['y']

correlation_coefficient, p_value = pearsonr(column1, column2)

# Print the correlation coefficient and p-value
print("Correlation coefficient:", correlation_coefficient)
print("P-value:", p_value)