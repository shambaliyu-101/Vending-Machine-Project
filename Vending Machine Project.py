import tkinter as tk
from tkinter import messagebox

class VendingMachine:
    def __init__(self, master):
        self.master = master
        self.master.title("Vending Machine")

        # Inventory: Item name, price, quantity
        self.inventory = {
            "Chips": [1.5, 10],
            "Soda": [1.0, 8],
            "Candy": [0.75, 15],
            "Water": [1.25, 12]
        }

        self.balance = 0.0

        # UI Setup
        self.create_ui()

    def create_ui(self):
        tk.Label(self.master, text="Welcome to the Vending Machine", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        self.item_frame = tk.Frame(self.master)
        self.item_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.display_inventory()

        self.balance_label = tk.Label(self.master, text=f"Balance: $0.00", font=("Arial", 14))
        self.balance_label.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Label(self.master, text="Insert Money:").grid(row=3, column=0, sticky="e")
        self.money_entry = tk.Entry(self.master)
        self.money_entry.grid(row=3, column=1, sticky="w")

        self.insert_button = tk.Button(self.master, text="Insert", command=self.insert_money)
        self.insert_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.clear_button = tk.Button(self.master, text="Reset Balance", command=self.reset_balance)
        self.clear_button.grid(row=5, column=0, columnspan=2, pady=5)

    def display_inventory(self):
        for widget in self.item_frame.winfo_children():
            widget.destroy()

        for index, (item, details) in enumerate(self.inventory.items()):
            item_label = tk.Label(self.item_frame, text=f"{item} - ${details[0]:.2f} ({details[1]} left)")
            item_label.grid(row=index, column=0, sticky="w")
            
            buy_button = tk.Button(self.item_frame, text="Buy", command=lambda i=item: self.purchase_item(i))
            buy_button.grid(row=index, column=1)

    def insert_money(self):
        try:
            amount = float(self.money_entry.get())
            if amount > 0:
                self.balance += amount
                self.update_balance()
                self.money_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Invalid Input", "Please enter a positive amount.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

    def reset_balance(self):
        self.balance = 0.0
        self.update_balance()

    def purchase_item(self, item):
        price, quantity = self.inventory[item]
        if quantity <= 0:
            messagebox.showinfo("Out of Stock", f"{item} is out of stock.")
            return

        if self.balance >= price:
            self.balance -= price
            self.inventory[item][1] -= 1
            self.update_balance()
            self.display_inventory()
            messagebox.showinfo("Success", f"You bought {item} for ${price:.2f}.")
        else:
            messagebox.showerror("Insufficient Balance", f"{item} costs ${price:.2f}. Please insert more money.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VendingMachine(root)
    root.mainloop()
