import sqlite3
with sqlite3.connect("shopping2.db") as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shopping2 (
                   id INTEGER PRIMARY KEY,
                   product TEXT,
                   amount INTEGER
                     );
                   """)
    
    conn.commit()
    

    while True:
        print("1. Fügen Sie ein Produkt hinzu")
        print("2. Produkte anzeigen")
        print("3. Produkte löschen")
        print("4. Beenden")
        choice= input("Wahlen Sie eine Option: ")
        if choice == "1":
            product = input("Fügen Sie ein Produkt hinzu: ")
            amount = int(input("Wie viele?"))
            if product and amount > 0:
                cursor.execute("INSERT INTO shopping2 (product, amount) VALUES (?, ?);", (product, amount))
                conn.commit()
            else:
                print("Ungültige Eingabe.")
        elif choice == "2":
            cursor.execute("SELECT * FROM shopping2;")
            rows = cursor.fetchall()
            for row in rows:
                print(f"Produkt: {row[1]}, Menge: {row[2]}")
        elif choice == "3":
            product = input("Welches Produkt möchten Sie löschen?")
            cursor.execute("DELETE FROM shopping2 WHERE product = ?;", (product,))
            conn.commit()
            print("Gelöscht")
        elif choice == "4":
            break
        else:
            print("Ungültige Option.")



        
