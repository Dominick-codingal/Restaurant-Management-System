import tkinter as tk
from tkinter import messagebox

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        root.title("Restaurant App")

        # Menu with section titles marked by None
        self.menu = {
            "Non-Veg Options": None,
            "Cheese Burger": 2.99,
            "Steak": 5.99,
            "Fries": 2.50,
            "Pizza": 7.99,
            "Veg Options": None,
            "Veg Pizza": 7.99,
            "Veg Burger": 3.99,
            "Sodas": None,
            "Pepsi": 0.99,
            "Coke": 0.99,
        }

        tk.Label(root, text="Restaurant Menu", font=("Times New Roman", 18)).pack(pady=10)
        self.entries = {}

        for item, price in self.menu.items():
            if price is None:
                # Section title
                tk.Label(root, text=item, font=("Arial", 14, "bold")).pack(pady=(10, 0))
                continue

            frame = tk.Frame(root)
            frame.pack()
            tk.Label(frame, text=f"{item} (${price})", width=20).pack(side="left")
            entry = tk.Entry(frame, width=5)
            entry.pack(side="left")
            self.entries[item] = entry

        tk.Button(root, text="Place Order", command=self.place_order).pack(pady=20)

    def place_order(self):
        total = 0
        summary = "Order Summary:\n"
        for item, entry in self.entries.items():
            qty = entry.get()
            if qty.isdigit():
                qty = int(qty)
                cost = qty * self.menu[item]
                total += cost
                if qty > 0:
                    summary += f"{item}: {qty} x ${self.menu[item]} = ${cost:.2f}\n"

        if total > 0:
            summary += f"\nTotal: ${total:.2f}"
            messagebox.showinfo("Order Placed", summary)
        else:
            messagebox.showwarning("Order Not Placed", "Please enter item quantities.")

# Running the app
root = tk.Tk()
app = RestaurantApp(root)
root.mainloop()
