# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

import numpy as np

x1 = float(input("Enter x-coordinate of the first point: "))
y1 = float(input("Enter y-coordinate of the first point: "))

x2 = float(input("Enter x-coordinate of the second point: "))
y2 = float(input("Enter y-coordinate of the second point: "))

point1 = np.array([x1, y1])
point2 = np.array([x2, y2])

distance = np.linalg.norm(point2 - point1)

print("Euclidean distance:", distance)
