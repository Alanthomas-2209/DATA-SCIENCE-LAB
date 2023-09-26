import numpy as np
from collections import Counter

num_rolls = 1000
dice_rolls = np.random.randint(1, 7, num_rolls)

counts = Counter(dice_rolls)

for number, count in counts.items():
    print(f"Number {number}: {count} occurrences")
