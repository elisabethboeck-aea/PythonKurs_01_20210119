secret = 18

for i in range(3):
    guess = int(input("Bitte Zahl (zwischen 1 und 30) raten: "))
    if guess == secret:
        print("Gewonnen! Die Zahl ist " + str(secret))
        break # beendet nur  die schleife, exit() beendet das gesamte Programm
    else:
        print("Falsch. Die richtige Zahl war nicht " + str(guess))
        print(i)