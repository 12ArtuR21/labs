import time
def generate_bouquets(K, N):
    allbuket = []  # Здесь будем хранить все найденные букеты
    buket = []   # Текущий формируемый букет
    def backtrack(start, length):
        if length > N:
            return
        if length >= 1:
            allbuket.append(buket.copy())
        for flower_type in range(start, K + 1):
            buket.append(flower_type)
            backtrack(flower_type, length + 1)
            buket.pop()
    backtrack(1, 0)
    return allbuket
K=int(input())
N=int(input())
start_time = time.time()
result = generate_bouquets(K, N)
end_time = time.time()
for i in result:
    print(i)
print(f"Время выполнения: {end_time - start_time:.5f} секунд")