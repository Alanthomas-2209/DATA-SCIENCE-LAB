import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\MCA\Third  Sem\Lab\DATA-SCIENCE-LAB\CO1\NumPy, Matplotlib Questions\CompanySalesData.csv')

df['total_profit'] = df['facecream'] + df['facewash'] + df['toothpaste'] + df['bathingsoap'] + df['shampoo'] + df['moisturizer']

line_style = '--'
line_color = 'red'
marker = 'o'
marker_color = 'red'
line_width = 3

plt.plot(df['month_number'], df['total_profit'], linestyle=line_style, color=line_color, marker=marker, markersize=8, markerfacecolor=marker_color, linewidth=line_width, label='Total Profit')

plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Total Profit of All Months')

plt.legend(loc='lower right')

plt.grid(True)
plt.show()

