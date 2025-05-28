from itertools import combinations_with_replacement
import time
def generate_bouquets(K, N):
    flower_types = range(1, K + 1)
    all_bouquets = []
    for m in range(1, N + 1):
        bouquets = combinations_with_replacement(flower_types, m)
        all_bouquets.extend(bouquets)
    return all_bouquets
N = int(input())
K = int(input())
start_time = time.time()
result = generate_bouquets(K, N)
end_time = time.time()
for i in result:
    print(i)
print(f"Время выполнения: {end_time - start_time:.5f} секунд")