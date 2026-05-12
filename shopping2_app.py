
import tkinter as tk
from tkinter import simpledialog
import sqlite3
from PIL import Image, ImageTk

def verbinden():
    return sqlite3.connect(r"C:\Users\Student\OneDrive - GFN GmbH (EDU)\Dokumente\My Python\shopping2.db")
def hinzufügen():
    window.lift()
    window.focus_force()
    produkt = simpledialog.askstring("Produkt", "Welches Produkt?", parent = window)
    menge = simpledialog.askinteger("Menge", "Wie viel?", parent = window)
    if produkt and menge:
        with verbinden() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO shopping2 (product, amount)VALUES (?, ?);", (produkt, menge))
            conn.commit()
def anzeigen():
    listbox.delete(0, tk.END)
    with verbinden() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM shopping2;")
        produkte = cursor.fetchall()
    for produkt in produkte:
        listbox.insert(tk.END, f"{produkt[1]}: {produkt[2]}")
def löschen():
    produkt = simpledialog.askstring("Produkt löschen", "Welches Produkt soll gelöscht werden?")
    if produkt:
        with verbinden() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM shopping2 WHERE product = ?", (produkt,))
            conn.commit()

def tabelle_erstellen():
    with verbinden() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS shopping2 (
                       id INTEGER PRIMARY KEY,
                       product TEXT,
                       amount INTEGER
                         );
                       """)
        conn.commit()
tabelle_erstellen()

window = tk.Tk()
window.title("Shopping List")
window.geometry("400x500")
window.configure(bg = "lightyellow")

icon = ImageTk.PhotoImage(Image.open(r"C:\Users\Student\OneDrive - GFN GmbH (EDU)\Dokumente\My Python\shopping2.png.png"))
window.iconphoto(True, icon)
button = tk.Button(window, text = "Produkt hinzufügen", bg="lightgreen", fg="darkgreen", width=20, command=hinzufügen)
button.pack(anchor="nw", pady=5)
button2 = tk.Button(window, text = "Produkte anzeigen", bg="lightgreen", fg="darkgreen", width=20, command=anzeigen)
button2.pack(anchor="nw", pady=5)
button3 = tk.Button(window, text = "Produkt löschen", bg="lightgreen", fg="darkgreen", width=20, command=löschen)
button3.pack(anchor="nw", pady=5)

listbox = tk.Listbox(window, width=40, height=20, bg="orange", fg="darkred")
listbox.pack(pady=10)

window.mainloop()
