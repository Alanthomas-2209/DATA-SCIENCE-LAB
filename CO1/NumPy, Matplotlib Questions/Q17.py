# 17.	Normal Distribution Plot using Numpy and Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Get user input for mean, standard deviation, and number of data points
mean = float(input("Enter the mean of the distribution: "))
std_dev = float(input("Enter the standard deviation of the distribution: "))
num_samples = int(input("Enter the number of data points: "))

# Set the seed for reproducibility (optional)
np.random.seed(0)

# Generate random numbers from a normal distribution
data = np.random.normal(mean, std_dev, num_samples)

# Create a histogram to visualize the distribution
plt.hist(data, bins=30, density=True, alpha=0.6, color='b')

# Add labels and a title
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Normal Distribution')

# Plot the probability density function (PDF) of the normal distribution
x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 1000)  # Range of x values
pdf = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
plt.plot(x, pdf, 'r', linewidth=2)

# Show the plot
plt.show()
