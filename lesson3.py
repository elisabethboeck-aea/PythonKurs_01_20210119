# Beispiel: Eingabe Zahl zwischen 1 und 100, alle Zahlen bis zu Eingabe werden gezeigt, wenn Ausgabezahl/3 dann wird "fizz" ausgegeben, bei /5 "buzz"
# wenn beides zutrifft (/3 und /5) "fizzbuzz"

# Anmerkung: % ist der der modulo Opperator, dieser prüft, ob bei Division ein Rest bleibt. Für Prozentrechnung muss tatsächlich /100 dividiert werden!

end_zahl = int(input("Bitte Zahl zwischen 1 und 100 eingeben: "))

for number in range(1, end_zahl + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print ("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

