#while true Schleife

import random # importiert fertige funktionen/bibliotheken

secret = random.randint(1, 30)
# bool_a = True # als Steuervariable, dann while bool_a und bool_a = False als Ausstieg

while True:
    guess = int(input("Bitte Zahl (zwischen 1 und 30) raten: "))
    if guess == secret:
        print("Gewonnen! Die Zahl ist " + str(secret))
        break
    elif guess > secret:
        print("Falsch, die gesuchte Zahl ist kleiner.")
    elif guess < secret:
        print("Falsch, die gesuchte Zahl ist größer.")
