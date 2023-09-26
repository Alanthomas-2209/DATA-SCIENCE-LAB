import matplotlib.pyplot as plt

x_str = input("Enter x-values (comma-separated): ")
y_str = input("Enter y-values (comma-separated): ")

x = [float(val) for val in x_str.split(',')]
y = [float(val) for val in y_str.split(',')]

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data Points')

plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend() 

plt.show()
