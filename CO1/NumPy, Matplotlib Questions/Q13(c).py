# c.	Calculate total sale data for last year for each product and show it using a Pie chart

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'CO1\NumPy, Matplotlib Questions\CompanySalesData.csv')

last_year_sales = df.iloc[-12:, 1:7].sum()  

product_names = df.columns[1:7]

plt.figure(figsize=(8, 8))
plt.pie(last_year_sales, labels=product_names, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales for Each Product (Last Year)')

plt.axis('equal')  
plt.show()
