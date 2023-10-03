# b.	Display the number of units sold per month for each product using multi- line plots. 
# (i.e., Separate Plotline for each product ). 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'CO1\NumPy, Matplotlib Questions\CompanySalesData.csv')

line_styles = ['-', '--', '-.', ':', '-', '--']  
colors = ['red', 'blue', 'green', 'purple', 'orange', 'pink']  
markers = ['o', 's', '^', 'D', 'v', 'x']  
line_width = 2

for i, product in enumerate(['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']):
    plt.plot(df['month_number'], df[product], linestyle=line_styles[i], color=colors[i], marker=markers[i], markersize=6, linewidth=line_width, label=product)

plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Number of Units Sold Per Month (By Product)')

plt.legend(loc='upper left')

plt.grid(True)
plt.show()
