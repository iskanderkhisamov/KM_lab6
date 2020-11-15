import matplotlib.pyplot as plt
import numpy as np

n = 30 + 1 + 4
p = 0.02 * 1 + 0.01 * 4
s = np.random.poisson(n * p, 200)

print('Количество значений: 200')
print('n:', n)
print('p:', p)

print('\nЗначения:')
for i in range(len(s)):
    print(str(i + 1) + ':', s[i])

print('\nМатематическое ожидание: ', np.mean(s))
print('Дисперсия: ', np.var(s))
print('Выборочное среднее: ', np.sum(s) / len(s))
print('Среднее квадратичное отклонение', np.std(s))

plt.hist(s, bins=8, edgecolor='black')
plt.xlabel('Числа')
plt.ylabel('Частота')
plt.show()
