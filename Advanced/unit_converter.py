# Install Required Libraries
# pip install pint
# pip install pint-pandas
# pip install pandas

import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.configure(bg="#f0f4f7")

# Input value
label_value = ttk.Label(root, text="Value:", background="#f0f4f7")
label_value.pack(pady=5)
entry_value = ttk.Entry(root, font=("Helvetica", 12), width=20)
entry_value.pack(pady=5)

# Dropdown for "from" unit
label_from = ttk.Label(root, text="Convert from:", background="#f0f4f7")
label_from.pack(pady=5)
unit_from_var = tk.StringVar()
combo_from = ttk.Combobox(root, textvariable=unit_from_var, font=("Helvetica", 10))
combo_from["values"] = list(conversion_map.keys())
combo_from.pack(pady=5)

# Dropdown for "to" unit
label_to = ttk.Label(root, text="Convert to:", background="#f0f4f7")
label_to.pack(pady=5)
unit_to_var = tk.StringVar()
combo_to = ttk.Combobox(root, textvariable=unit_to_var, font=("Helvetica", 10))
combo_to.pack(pady=5)

# Convert button
button_convert = ttk.Button(root, text="Convert", command=None)
button_convert.pack(pady=10)

# Result label
label_result = ttk.Label(root, text="", font=("Helvetica", 14), background="#f0f4f7", foreground="#333")
label_result.pack(pady=20)