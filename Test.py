# Цей застосунок містить навмисні помилки UI/UX та функціональні помилки
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root

        self.root.title("Конвертер валют (версія 2)")

        self.root.geometry("400x350")
        
        # Функціональна помилка №3: історія додається, але завжди очищується
        self.history = []  # список для історії
        
        # UI/UX помилка 1: відсутня підказка щодо формату валюти
        tk.Label(root, text="Введіть суму (UAH)").pack(pady=5)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()
        
        # UI/UX помилка 2: поле для введення замість списку
        tk.Label(root, text="Валюта (USD/EUR/PLN)").pack()
        self.currency_var = tk.StringVar()
        self.currency_combo = ttk.Combobox(root, textvariable=self.currency_var, values=["USD", "EUR", "PLN"])
        self.currency_combo.pack()
        
        # Функціональна помилка 1: виклик методу з помилкою в назві 
        tk.Button(root, text="Конвертувати", command=self.wrong_convert).pack(pady=10)
        
        self.result_label = tk.Label(root, text="Результат: ")
        self.result_label.pack()
        
        # Кнопка для перегляду історії (показує пустий список через помилку)
        tk.Button(root, text="Показати історію", command=self.show_history).pack(pady=5)
        
        # UI/UX помилка 3: очищення без відновлення фокуса
        tk.Button(root, text="Очистити", command=self.clear_all).pack()
    
    def wrong_convert(self):
        try:
            amount = float(self.amount_entry.get())
            currency = self.currency_var.get()
            # Функціональна помилка 2: неправильна формула (множення замість ділення)
            rates = {"USD": 27.5, "EUR": 33.0, "PLN": 6.8}
            if currency in rates:
                result = amount / rates[currency]
                self.result_label.config(text=f"Результат: {result} {currency}")
                
                # Функціональна помилка №3: зберігаємо в історію, АЛЕ з помилкою
                self.history.clear()
                self.history.append(f"{amount} UAH -> {result} {currency}")
            else:
                messagebox.showerror("Помилка", "Невідома валюта")
        except ValueError:
            messagebox.showerror("Помилка", "Введіть число")
    
    def show_history(self):
        # Через помилку clear() історія завжди пуста, навіть після конвертацій
        if not self.history:
            messagebox.showinfo("Історія", "Історія конвертацій порожня.")
        else:
            history_text = "\n".join(self.history)
            messagebox.showinfo("Історія", history_text)
    
    def clear_all(self):
        self.amount_entry.delete(0, tk.END)
        self.currency_entry.delete(0, tk.END)
        self.result_label.config(text="Результат: ")
        # фокус не встановлено на amount_entry

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
# Copyright 2026, for educational purposes
# Hello world