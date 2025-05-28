import math
import time
import matplotlib.pyplot as plt
def recursive_f(n):
    if n < 3:
        return 3
    elif 3 <= n <= 25:
        return recursive_f(n - 1)
    else:
        return (-1) ** n * (5 * recursive_f(n - 1) / math.factorial(2 * n) - 2 * (n - 2))
def iterative_f(n):
    if n < 3:
        return 3
    f = [0] * (n + 1)
    for i in range(3):
        f[i] = 3
    for i in range(3, n + 1):
        if i <= 25:
            f[i] = f[i - 1]
        else:
            f[i] = (-1) ** i * (5 * f[i - 1] / math.factorial(2 * i) - 2 * (i - 2))
    return f[n]
def compare_methods(max_n):
    recursive_times = []
    iterative_times = []
    n_values = list(range(1, max_n + 1))

    for n in n_values:
        # Измерение времени для рекурсивного метода
        start = time.time()
        recursive_f(n)
        end = time.time()
        recursive_times.append(end - start)

        # Измерение времени для итерационного метода
        start = time.time()
        iterative_f(n)
        end = time.time()
        iterative_times.append(end - start)

    return n_values, recursive_times, iterative_times

max_n = 30  # Выберем достаточно большое n для демонстрации
n_values, recursive_times, iterative_times = compare_methods(max_n)
print(recursive_times)
# Вывод таблицы
print("n\tРекурсия (с)\tИтерация (с)")
for n, rt, it in zip(n_values, recursive_times, iterative_times):
    print(f"{n}\t{rt:.6f}\t{it:.6f}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(n_values, recursive_times, label='Рекурсия')
plt.plot(n_values, iterative_times, label='Итерация')
plt.xlabel('n')
plt.ylabel('Время (с)')
plt.title('Сравнение времени вычисления функции')
plt.legend()
plt.grid()
plt.show()