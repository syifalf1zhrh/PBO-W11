import tkinter as tk

# List Marvel Series
marvel_series = [
    "Iron Man",
    "Avengers : Endgame",
    "The Falcon and the Winter Soldier",
    "WandaVision",
    "Black Widow",
    "Thunderbolts",
    "Doctor Strange in the Multiverse of Madness",
    "Hawkeye",
    "Moon Knight",
    "Ms. Marvel",
    "Agatha: House of Harkness",
]

# Fungsi untuk menampilkan pilihan
def tampilkan_pilihan():
    pilihan = []
    for var, name in zip(checkbox_vars, marvel_series):
        if var.get():
            pilihan.append(name)
    hasil.config(text="Pilihan MCU Favorit kamu:\n" + "\n".join(pilihan))

# GUI setup
root = tk.Tk()
root.title("Marvel Cinematic Universe")
root.geometry("350x400")

judul = tk.Label(root, text="Pilih Kesukaan mu:", font=("Times New Roman", 12, "bold"))
judul.pack(pady=10)

checkbox_vars = []
for series in marvel_series:
    var = tk.BooleanVar()
    cb = tk.Checkbutton(root, text=series, variable=var)
    cb.pack(anchor='w', padx=20)
    checkbox_vars.append(var)

btn_tampilkan = tk.Button(root, text="Tampilkan Hasil", command=tampilkan_pilihan)
btn_tampilkan.pack(pady=15)

hasil = tk.Label(root, text="", justify="left")
hasil.pack()

root.mainloop()
