import tkinter as tk
import os
from tkinter import messagebox
import barcode
from barcode.writer import ImageWriter

def generate_barcode():
    code = entry_code.get().strip()
    filename = entry_filename.get().strip()
    user = os.getlogin()
    directory = os.path.expanduser(f"~{user}/Documents/Kody_Kreskowe")

    if not os.path.exists(directory):
        os.makedirs(directory)

    if not code or not filename:
        messagebox.showerror("Błąd", "Proszę wypełnić oba pola!")
        return

    if len(code) != 13 or not code.isdigit():
        messagebox.showerror("Błąd", "Kod musi mieć dokładnie 13 cyfr!")
        return

    try:
        EAN = barcode.get_barcode_class('ean13')
        my_ean = EAN(code, writer=ImageWriter())
        full_filename = os.path.join(directory, filename)

        print(f"Saving barcode to: {full_filename}")
        my_ean.save(full_filename)

        messagebox.showinfo("Sukces", f"Kod kreskowy zapisano w: {full_filename}")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")
        print(f"Error: {e}")

root = tk.Tk()
root.title("Generator kodów kreskowych")
root.geometry("300x200")

tk.Label(root, text="Wpisz 13-cyfrowy kod:").pack(pady=5)
entry_code = tk.Entry(root)
entry_code.pack(pady=5)

tk.Label(root, text="Nazwa pliku:").pack(pady=5)
entry_filename = tk.Entry(root)
entry_filename.pack(pady=5)

tk.Button(root, text="Generuj kod kreskowy", command=generate_barcode).pack(pady=20)

root.mainloop()

