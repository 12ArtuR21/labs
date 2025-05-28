import numpy as np
import matplotlib.pyplot as plt
N, K = input("Ввод N: "), input("Ввод K: ")
assert N.isdigit() and N. isalnum(), 'N должно быть целым числом'
assert K.isdigit() and K.isalnum(), 'K должно быть целым числом'
N,K,Summa,p,det,SummB,SummC,SummD,SummE = int(N),int(K),0,1,0,0,0,0,0
A= np.random.randint(-10, 10, size=(N, N))
F, O = np.copy(A), N%2
print('\nМатрица A:\n',A, '\n')
for x in range(N//2+O, N):
    for y in range(N//2+O, N):
        SummC += F[x][y]
        if y%2==0: Summa += F[x][y]
        if x%2!=0: p *= F[x][y]
if Summa>p:
    F[0:N//2, N//2+O:N], F[N//2+O:N, N//2+O:N] = list(reversed(F[N//2+O:N, N//2+O:N])), list(reversed(A[0:N//2, N//2+O:N]))
    print('Поменяли B и С симметрично:\n', F,'\n')
else:
    F[0:N//2, 0:N//2], F[0:N//2, N//2+O:N] = F[0:N//2, N//2+O:N], A[0:N//2, 0:N//2]
    print('Поменяли Е и В не симметрично:\n', F,'\n')
if N%2==1: total_sum = np.trace(F) + np.trace(np.fliplr(F)) - F[N//2, N//2]
else: total_sum = np.trace(F) + np.trace(np.fliplr(F))
if np.linalg.det(A) != 0 and np.linalg.det(A) > total_sum: print('Результат:\n',np.add(np.dot(np.linalg.inv(A), A.T), np.dot(np.linalg.inv(F), K)))
if np.linalg.det(A) != 0 and np.linalg.det(A) < total_sum: print('\nРезультат:\n',np.dot(np.subtract(np.add(A.T, np.linalg.inv(np.tril(A))), np.linalg.inv(F)), K))
for x in range(0, N//2):
    for y in range(0, N//2):
        SummE += F[x][y]
for x in range(0, N//2+O):
    for y in range(N//2+O, N):
        SummB += F[x][y]
for x in range (N//2+O,N):
    for y in range (0, N//2+O):
        SummD += F[x][y]
ydata = [SummE, SummB, SummC, SummD]
xdata, xnum = ["E", "B", "C", "D"], []
for x in range(0, N): xnum.append(x)
plt.tight_layout()
plt.subplot(1,3,1)
plt.bar(xdata, ydata)
plt.title("Столбчатая диаграмма")
plt.xlabel('Область')
plt.ylabel('Сумма')
plt.grid(True)

plt.subplot(1,3,2)
plt.imshow(F, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(np.arange(min(xnum), max(xnum)+1, 1.0))
plt.yticks(np.arange(min(xnum), max(xnum)+1, 1.0))
plt.title("Тепловая карта")

plt.subplot(1,3,3)
plt.plot(xdata, ydata)
plt.title("Линейный график")
plt.xlabel("Область")
plt.ylabel('Сумма элементов')
plt.show()