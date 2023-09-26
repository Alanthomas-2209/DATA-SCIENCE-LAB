# 16.	Plot a complex number in Python using Matplotlib 

import matplotlib.pyplot as plt

real_part = float(input("Enter the real part of the complex number: "))
imaginary_part = float(input("Enter the imaginary part of the complex number: "))

complex_number = complex(real_part, imaginary_part)

real_part = complex_number.real
imaginary_part = complex_number.imag

plt.figure(figsize=(6, 6))
plt.scatter(real_part, imaginary_part, color='red', marker='o', label='Complex Number')


plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

# plt.legend()

plt.grid(True)

plt.title('Complex Number Plot')

plt.show()
