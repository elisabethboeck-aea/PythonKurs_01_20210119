a = 33
b = "Hello"
c = [1, 2, 3]

a = 0
b = a
b += 20 # b = b + 20
print(a)
print(id(a))
print(id(b))
print(id(a) == id(b))

a = [1, 2, 3]
b = a
b += [55]
print(a)
print(id(a) == id(b))

# int, float, bool, String, None -> wird per value übergeben
# array, dict, object -> wird als referenz zum Speicherplatz weiter gegeben

a = [1, 2, 3]
b = a
b = [1, 2, 3]
b[0] = 42
print(a)
print(b)

# kopieren:
def make_value_42(b):
    b[0] = 42

a = [1, 2, 3]
make_value_42(a)
print(a)

a = [1, 2, 3]
b = list(a) # b = a gibt die referenz auf die Liste aus, list() kopiert die liste, aber legt eine neue Referenz an
b[0] = 42
print(a)
print(b)


# ACHTUNG:
a = [1, 2, [3]]
b = list(a) # der dritte wert ist eine Liste in einer Liste, daher funktioniert das in diesem Fall nicht. Die list-funktion bezieht sich nur auf die erste Ebene der Liste
b[2] += [42]
print(a)
print(b)
# Lösung:
from copy import deepcopy # deepcopy funktioniert für alle typen, egal ob integer, list, object, auch wenn liste in liste, object in liste etc.
a = [1, 2, [3]]
b = deepcopy(a)
b[2] += [42]
print(a)
print(b)


a = []
a.append(a)
print(a)
b = deepcopy(a)

# Objekte:

class Thing(object):
    test = []

a = Thing()
b = Thing()
b.test.append(42)
print(a.test) # enthält jetzt auch 42, weil die Liste "test" einen Speicherplatz belegt und der für a und b gleich ist

#richtige Lösung:
class Thing(object):
    def __init__(self): # init erstellt/initialisiert neue Objekte, die auch einen eigenen Speicherplatz haben
        self.test = []

a = Thing()
b = Thing()
b.test.append(42)
print(a.test)
print(b.test)
print(id(a))
print(id(b))
b.test.append(100)
print(id(b))
print(b.test)
print(id(b.test[1]))