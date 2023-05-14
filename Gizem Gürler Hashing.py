import tkinter as tk
from tkinter import filedialog
import hashlib

def open_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)

def calculate_hash():
    file_path = file_entry.get()
    hash_algorithm = hash_dropdown.get()

    if file_path:
        try:
            hash_func = hashlib.new(hash_algorithm)
            with open(file_path, 'rb') as file:
                while True:
                    data = file.read(4096)
                    if not data:
                        break
                    hash_func.update(data)

            hash_value = hash_func.hexdigest()
            hash_output.delete(0, tk.END)
            hash_output.insert(tk.END, hash_value)
        except IOError:
            hash_output.delete(0, tk.END)
            hash_output.insert(tk.END, "Dosya okunamadı.")
    else:
        hash_output.delete(0, tk.END)
        hash_output.insert(tk.END, "Dosya seçilmedi.")

def verify_hash():
    file_path = file_entry.get()
    input_hash = input_hash_entry.get()
    hash_algorithm = hash_dropdown.get()

    if file_path:
        try:
            hash_func = hashlib.new(hash_algorithm)
            with open(file_path, 'rb') as file:
                while True:
                    data = file.read(4096)
                    if not data:
                        break
                    hash_func.update(data)

            hash_value = hash_func.hexdigest()
            if hash_value == input_hash:
                verification_label.config(text="Hash doğrulandı.")
            else:
                verification_label.config(text="Hash doğrulanmadı.")
        except IOError:
            verification_label.config(text="Dosya okunamadı.")
    else:
        verification_label.config(text="Dosya seçilmedi.")

# GUI oluşturma
window = tk.Tk()
window.title("Hashing Uygulaması")

# Dosya seçme bölümü
file_label = tk.Label(window, text="Dosya Seçin:")
file_label.pack()

file_entry = tk.Entry(window, width=50)
file_entry.pack()

file_button = tk.Button(window, text="Dosya Seç", command=open_file)
file_button.pack()

# Hash çıktısı hesaplama bölümü
hash_label = tk.Label(window, text="Hash Algoritması:")
hash_label.pack()

hash_dropdown = tk.StringVar(window)
hash_dropdown.set("md5")  # Varsayılan olarak md5 seçili

hash_menu = tk.OptionMenu(window, hash_dropdown, "md5", "sha1", "sha256")
hash_menu.pack()

calculate_button = tk.Button(window, text="Hash Hesapla", command=calculate_hash)
calculate_button.pack()

hash_output = tk.Entry(window, width=50)
hash_output.pack()

# Hash doğrulama bölümü
input_hash_label = tk.Label(window, text="Doğrulanacak Hash:")
input_hash_label.pack()

input_hash_entry = tk.Entry(window, width=50)
input_hash_entry.pack()

verify_button = tk.Button(window, text="Hash Doğrula", command=verify_hash)
verify_button.pack()

verification_label = tk.Label(window, text="")
verification_label.pack()

window.mainloop()
