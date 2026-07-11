import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# Separate sales by gender
male_sales = df[df["Gender"] == "Male"]["Total_Sales"]
female_sales = df[df["Gender"] == "Female"]["Total_Sales"]

# Calculate average sales
print("Male Average Sales:", male_sales.mean())
print("Female Average Sales:", female_sales.mean())

# Perform Independent Samples t-test
t_stat, p_value = ttest_ind(male_sales, female_sales)

# Display results
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Decision
if p_value < 0.05:
    print("Reject the Null Hypothesis")
else:
    print("Fail to Reject the Null Hypothesis")