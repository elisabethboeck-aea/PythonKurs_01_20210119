## Importieren von einzelnen Funktionen aus der functions Bibliothek

#from functions import say_hello - diese variante braucht weniger Rechenleistung - ist also bei großen Programmen mit vielen Bibliotheken zu bevorzugen
#from functions import say_goodbye

#say_hello()
#say_goodbye()

## alternative variante (gesamte Bibliothek functions importieren, dann einzelne funktionen anwenden)

import functions
functions.say_hello()
functions.say_goodbye()
functions.say_hello()