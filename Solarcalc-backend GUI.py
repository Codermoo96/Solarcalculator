import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        if monthly_input.get() == "Nej":
            annual = int(annual_entry.get())
            monthly_consumption = [
                annual * 0.14, annual * 0.13, annual * 0.12,
                annual * 0.09, annual * 0.06, annual * 0.04,
                annual * 0.03, annual * 0.04, annual * 0.05,
                annual * 0.08, annual * 0.11, annual * 0.13
            ]
        else:
            monthly_consumption = []
            for entry in month_entries:
                monthly_consumption.append(int(entry.get()))
            annual = sum(monthly_consumption)

        recommended_solar = int(annual * 0.4)
        solar_distribution = [0.015, 0.025, 0.104, 0.13, 0.139, 0.134,
                              0.135, 0.120, 0.095, 0.057, 0.027, 0.019]
        monthly_production = [int(recommended_solar * p) for p in solar_distribution]
        battery_size = int((recommended_solar / 12) / 30)

        # Clear output
        output_text.delete("1.0", tk.END)

        # Print consumption
        output_text.insert(tk.END, f"Årlig förbrukning: {int(annual)} kWh\n\n")
        output_text.insert(tk.END, "Månadsförbrukning:\n")
        for i, month in enumerate(months):
            output_text.insert(tk.END, f"{month}: {int(monthly_consumption[i])} kWh\n")
        output_text.insert(tk.END, f"\nRekommenderad solproduktion: {recommended_solar} kWh\n\n")
        output_text.insert(tk.END, "Månadsproduktion:\n")
        for i, month in enumerate(months):
            output_text.insert(tk.END, f"{month}: {monthly_production[i]} kWh\n")
        output_text.insert(tk.END, f"\nRekommenderad batteristorlek: {battery_size} kWh (daglig kapacitet)\n")

    except ValueError:
        messagebox.showerror("Fel", "Vänligen fyll i alla siffror korrekt.")

def toggle_monthly_inputs(*args):
    if monthly_input.get() == "Ja":
        annual_entry.configure(state="disabled")
        for entry in month_entries:
            entry.configure(state="normal")
    else:
        annual_entry.configure(state="normal")
        for entry in month_entries:
            entry.configure(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("Solcellsberäkning")
root.geometry("500x700")

monthly_input = tk.StringVar(value="Nej")
monthly_input.trace("w", toggle_monthly_inputs)

tk.Label(root, text="Vet du kundens förbrukning månadsvis?").pack()
tk.OptionMenu(root, monthly_input, "Ja", "Nej").pack()

tk.Label(root, text="Årsförbrukning (kWh):").pack()
annual_entry = tk.Entry(root)
annual_entry.pack()

months = ["Januari", "Februari", "Mars", "April", "Maj", "Juni",
          "Juli", "Augusti", "September", "Oktober", "November", "December"]

month_entries = []
for month in months:
    tk.Label(root, text=month).pack()
    entry = tk.Entry(root, state="disabled")
    entry.pack()
    month_entries.append(entry)

tk.Button(root, text="Beräkna", command=calculate).pack(pady=10)

output_text = tk.Text(root, height=20, width=60)
output_text.pack()

root.mainloop()
