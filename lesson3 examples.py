print(20 % 5)
print(20 % 3)

string_one = "Hallo"
string_two = "Lockdown"

print(string_one + " " + string_two)
print("{0} {1}".format(string_one, string_two)) # printet einen string, der aus Element 0 und Element 1 entsteht. So wird das Format definiert, dann werden die Inhalte der Elemente bekannt gegeben
print("{0} Li, willkommen im {1}".format(string_one, string_two))
print("%s %s" % (string_one, string_two)) # selbes Ergebnis wie oben, % ist hier kein Modulo, sondern repräsentiert etwas. %s = string, %d = dezimalzahl, ... ABER: sollte für solche Ausgaben nicht genutzt werden!
print(f"{string_one} {string_two}") # erst ab Python Version 3.6

# siehe Link https://realpython.com/python-string-formatting/ dafür

string_one.lower() # macht alles in Kleinbuchstaben, aber so wird das nirgends gespeichert - man müsste z.B. x = string_one.lower() machen und dann x printen
print(string_one.lower()) # so wird direkt in kleinbuchstaben geprintet

# wenn etwas importiert wird (z.b eine Bibliothek wie random, dann wird .(function) auf ??? angewendet. Wenn vor dem . eine variable steht, wird die funktion auf die variable angewendet

# Best practises bezüglich Code-Formatierung: https://www.python.org/dev/peps/pep-0008/ (Style Guide for Python Code)
