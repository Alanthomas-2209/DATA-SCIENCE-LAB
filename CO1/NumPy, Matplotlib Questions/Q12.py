import matplotlib.pyplot as plt

data = [
    {"x": 1, "y": 5, "label": "A", "color": "red", "marker": "o"},
    {"x": 2, "y": 4, "label": "B", "color": "blue", "marker": "^"},
    {"x": 3, "y": 6, "label": "C", "color": "green", "marker": "s"},
    {"x": 4, "y": 3, "label": "D", "color": "purple", "marker": "D"},
]

for point in data:
    plt.scatter(point["x"], point["y"], label=point["label"], color=point["color"], marker=point["marker"])

plt.title('Scatter Plot with Labeled Data Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()


plt.show()

# import matplotlib.pyplot as plt

# data = []

# while True:
#     x_str = input("Enter x-value (or type 'done' to finish): ")

#     if x_str.lower() == 'done':
#         break
    
#     y_str = input("Enter y-value: ")
#     label = input("Enter label: ")
#     color = input("Enter color (e.g., 'red', 'blue', 'green'): ")
#     marker = input("Enter marker (e.g., 'o', '^', 's', 'D'): ")

#     try:
#         x = float(x_str)
#         y = float(y_str)
#         data_point = {"x": x, "y": y, "label": label, "color": color, "marker": marker}
#         data.append(data_point)
#     except ValueError:
#         print("Invalid input. Please enter numeric values for x and y.")

# for point in data:
#     plt.scatter(point["x"], point["y"], label=point["label"], color=point["color"], marker=point["marker"])

# plt.title('Scatter Plot with Labeled Data Points')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()

# plt.show()
