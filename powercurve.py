from load_data import load_data
import numpy as np
from sort import bubble_sort
import matplotlib.pyplot as plt

data = load_data('activity.csv')
power_W = data['PowerOriginal']

N_steps = len(power_W)
zeit = np.arange(N_steps)

sorted_power_W = bubble_sort(power_W)

plt.plot(zeit, sorted_power_W[::-1])
plt.xlabel('Zeit in Sekunde')
plt.ylabel('Leistung in Watt')
plt.title('Power Curve')
plt.xlim(0)


plt.show()