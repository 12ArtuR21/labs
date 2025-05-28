from itertools import combinations_with_replacement
import time
from collections import Counter
def generate_bouquets(K, N, max_same):
    flower_types = range(1, K + 1)
    valid_bouquets = []
    for m in range(1, N + 1):
        for bouquet in combinations_with_replacement(flower_types, m):
            counts = Counter(bouquet)
            if all(v <= max_same for v in counts.values()):
                valid_bouquets.append(bouquet)
    return valid_bouquets
def most_unique(bouquets):
    return max(bouquets, key=lambda b: len(set(b)))
N = int(input())
K = int(input())
start_time = time.time()
result = generate_bouquets(K, N, 2)
most_unique = most_unique(result)
end_time = time.time()
for i in result:
    print(i)
print('Самый уникальный: ', most_unique)
print(f"Время выполнения: {end_time - start_time:.5f} секунд")