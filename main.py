"""
Простое графическое приложение для генерации случайного числа в заданном диапазоне.

Пользователь может задать минимальное и максимальное значения для двух слайдеров,
которые определяют диапазон. После нажатия на кнопку генерируется случайное число в этом диапазоне.
"""
import tkinter as tk
import random


def update_scales():
    """ Обновление диапазонов слайдеров согласно введенным значениям. """
    try:
        min_val = int(min_entry.get())
        max_val = int(max_entry.get())
        lower_scale.config(from_=min_val, to=max_val)
        upper_scale.config(from_=min_val, to=max_val)
    except ValueError:
        result_label.config(text="Ошибка: введите корректные числа")


def generate_random_number():
    """ Генерация случайного числа в заданном диапазоне. """
    lower = lower_scale.get()
    upper = upper_scale.get()
    if lower > upper:
        result_label.config(text="Ошибка: нижняя граница больше верхней")
    else:
        random_number = random.randint(lower, upper)
        result_label.config(text=f"Случайное число: {random_number}")


# Создание основного окна
root = tk.Tk()
root.title("Случайное число в диапазоне")

# Поля для ввода минимального и максимального значений
min_label = tk.Label(root, text="Минимум:")
min_label.pack(padx=10, pady=5)
min_entry = tk.Entry(root)
min_entry.pack(padx=10, pady=5)
min_entry.insert(0, "0")

max_label = tk.Label(root, text="Максимум:")
max_label.pack(padx=10, pady=5)
max_entry = tk.Entry(root)
max_entry.pack(padx=10, pady=5)
max_entry.insert(0, "100")

# Кнопка для обновления диапазонов слайдеров
update_button = tk.Button(root, text="Обновить диапазон", command=update_scales)
update_button.pack(pady=10)

# Слайдер для нижней границы
lower_scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
lower_scale.pack(padx=10, pady=10)
lower_scale.set(20)  # Установка начального значения

# Слайдер для верхней границы
upper_scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
upper_scale.pack(padx=10, pady=10)
upper_scale.set(80)  # Установка начального значения

# Кнопка для генерации числа
generate_button = tk.Button(root, text="Генерировать число", command=generate_random_number)
generate_button.pack(pady=10)

# Метка для вывода результата
result_label = tk.Label(root, text="Случайное число: ")
result_label.pack()

root.mainloop()
