import mysql.connector # Bibliothek im terminal mit pip install mysql-connector-python installiert

mydb = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11404167",
    password="TAVjHtFx7n",
    database="sql11404167"
)

mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS customerEBO" # SQL Befehle werden oft in variablen geschrieben, damit es übersichtlicher ist. Drop table löscht die Tabelle
mycursor.execute(sql)
mycursor.execute("CREATE TABLE customerEBO (name VARCHAR(255), address VARCHAR(255))") # erstellt eine Tabelle mit 2 Spalten in der Datenbank. Muss nur beim ersten Mal gemacht werden, sonst ist Fehlermeldung da, dass die Tabelle scho existiert
mycursor.execute("SHOW TABLES")
for tables in mycursor:
    print(tables)

mycursor.execute("ALTER TABLE customerEBO ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
sql = "INSERT INTO customerEBO (name, address) VALUES (%s, %s)"
# values = ("Elisabeth", "Straße 42") # nur ein Eintrag
# mycursor.execute(sql, values)  # geht nur, wenn es nur einen Eintrag gibt
values = [("Elisabeth", "Straße 42"), ("David", "Musterstraße 2"), ("Lisa", "Musterstraße 2")]
mycursor.executemany(sql, values) # executemany, wenn mehrere Datensätze eingelesen werden

mydb.commit() # Werden Datensätze in der DB bearbeitet, brauche ich diesen Befehl, damit die Datensätze bearbeitet werden

print(mycursor.rowcount, "Datensätze in der Datenbank.")
print("ID: ", mycursor.lastrowid)

sql = "SELECT * FROM customerEBO WHERE address = 'Musterstraße 2'"
mycursor.execute(sql)
#myresult = mycursor.fetchone()
#print(myresult)

myresult = mycursor.fetchall()
for result in myresult:
    print(result)

mydb.close()
