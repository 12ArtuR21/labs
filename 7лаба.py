from itertools import combinations_with_replacement
from collections import Counter
from tkinter import *
from tkinter import scrolledtext, messagebox


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

def on_run():
    try:
        N = int(entry_k.get())
        K = int(entry_n.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Ошибка")
        return
    gen = generate_bouquets(K, N, 2)
    uniq = most_unique(gen)
    output.config(state='normal')
    output.delete('1.0', END)
    output.insert(INSERT, f"Возможные варианты:\n{gen}\n\n")
    output.insert(INSERT, f"Самый оптимальный вариант:\n{uniq}\n")
    output.config(state='disabled')
# Главное окно ввода и вывода
root = Tk()
root.geometry("600x500")
root.title("Лаб. №6 – Алгоритмический метод и оптимизация")

# Фрейм для ввода
frame = Frame(root)
frame.pack(padx=10, pady=5)

# Ввод n
Label(frame, text="Количество видов: ", font=('Arial', 14)).grid(row=0, column=0, sticky="w")
entry_n = Entry(frame)
entry_n.grid(row=0, column=1, padx=5)

# Ввод минимальной суммы цифр m
Label(frame, text="Количество цветов: ", font=('Arial', 14)).grid(row=1, column=0, sticky="w")
entry_k = Entry(frame)
entry_k.grid(row=1, column=1, padx=5)

# Кнопка запуска
btn = Button(frame, text="Выполнить", font=('Arial', 14), command=on_run)
btn.grid(row=2, column=0, columnspan=2, pady=8)

# Поле вывода с прокруткой
output = scrolledtext.ScrolledText(root, width=60, height=20)
output.pack(padx=10, pady=5)
output.config(state='disabled')

root.mainloop()