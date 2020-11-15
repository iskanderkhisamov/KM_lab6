import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 1, 5
s = np.random.normal(mu, sigma, 100)

print('Количество значений: 100')
print('a:', mu)
print('σ:', sigma)

print('\nЗначения:')
for i in range(len(s)):
    print(str(i + 1) + ':', s[i])

plt.hist(s, bins=8, edgecolor='black')
plt.xlabel('Числа')
plt.ylabel('Частота')
plt.show()
