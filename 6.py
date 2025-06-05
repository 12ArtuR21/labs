import math
import timeit
import pandas as pd
import matplotlib.pyplot as plt

def rec_F(n):
    if n < 3:
        return 3
    if 3 <= n <= 25:
        return rec_F(n - 1)
    sign = 1 if n % 2 == 0 else -1
    return sign * (5 * rec_F(n - 1) / math.factorial(2 * n) - 2 * (n - 2))

def iter_F(n):
    if n <= 3:
        return 3
    F_prev = 3
    fact = 2
    for k in range(3, n + 1):
        fact *= (2 * k - 1) * (2 * k)
        if k <= 25:
            F_curr = F_prev
        else:
            sign = 1 if k % 2 == 0 else -1
            F_curr = sign * (5 * F_prev / fact - 2 * (k - 2))
        F_prev = F_curr
    return F_prev

if __name__ == '__main__':
    ns = list(range(0, 31))
    results = []
    for n in ns:
        t_rec = timeit.timeit(lambda: rec_F(n), number=10)
        t_it = timeit.timeit(lambda: iter_F(n), number=10)
        results.append((n, t_rec, t_it))
    df = pd.DataFrame(results, columns=['n', 'Recursive Time (s)', 'Iterative Time (s)'])
    print(df.to_string(index=False))

    plt.figure(figsize=(8, 5))
    plt.plot(df['n'], df['Recursive Time (s)'], '--o', label='Recursive')
    plt.plot(df['n'], df['Iterative Time (s)'], '-o', label='Iterative')
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('Сравнение времени: рекурсия vs итерация для F(n)')
    plt.legend()
    plt.grid(True)
    plt.show()
