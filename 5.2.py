from itertools import combinations_with_replacement
import time
from collections import Counter
def first_part(K, N):
    print('Усложненная первая часть:')
    allbuket = []
    buket = []
    unique = []
    def backtrack(start, length):
        if length > N:
            return
        if length >= 1:
            allbuket.append(buket.copy())
        for flower_type in range(start, K + 1):
            if buket.count(flower_type) < 2:
                buket.append(flower_type)
                backtrack(flower_type, length + 1)
                buket.pop()
    backtrack(1, 0)
    end_time = time.time()
    for i in allbuket:
        unique.append(list(set(i)))
    most_unique = max(unique, key=lambda b: len(set(b)))
    for i in allbuket:
        print(i)
    print('Уникальный букет: ', most_unique)
    print(f"Время выполнения: {end_time - start_time:.5f} секунд")
def second_part(K, N, max_same):
    print('\nУсложненная вторая часть:')
    flower_types = range(1, K + 1)
    valid_bouquets = []
    for m in range(1, N + 1):
        for bouquet in combinations_with_replacement(flower_types, m):
            counts = Counter(bouquet)
            if all(v <= max_same for v in counts.values()):
                valid_bouquets.append(bouquet)
    most_unique = max(valid_bouquets, key=lambda b: len(set(b)))
    end_time = time.time()
    for i in valid_bouquets:
        print(i)
    print('Уникальный букет: ', most_unique)
    print(f"Время выполнения: {end_time - start_time:.5f} секунд")
N = int(input())
K = int(input())
start_time = time.time()
first_part(K, N)
start_time = time.time()
second_part(K, N, 2)
