import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



sales = pd.read_csv('sales_data.csv', parse_dates=['Date'], dayfirst=True)
print(sales.head())
cusAge = sales['Customer_Age'].mean()
roundAge = round(cusAge , 1)
print(f"The mean age of customer is {roundAge}")

print(sales.columns)
print(sales.shape)
print(sales.info())
print(sales.describe())

unitMean = sales['Unit_Cost'].mean()
Unitmed = sales['Unit_Cost'].median()
unitDes = sales['Unit_Cost'].describe()
print(f" The mean of the unit cost: {unitMean}")
print(f"The median of the unit cost: {Unitmed}")
print(f"The description of the unit cost: \n{unitDes}")
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
plt.show()

sales['Unit_Cost'].plot(kind='density', figsize=(14,6))
plt.show()

ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6))
ax.axvline(sales['Unit_Cost'].mean(), color='red')
ax.axvline(sales['Unit_Cost'].median(), color='green')
plt.show()

ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
ax.set_xlabel('Number of sales')
ax.set_ylabel('Dollars')
plt.show()

agecount =  sales['Age_Group'].value_counts()
sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6))
plt.show()

