# loops / Schleifen

# Beispiel var_a, var_b = 10, 6

# secret = 11

# guess = int(input("Bitte Zahl (zwischen 1 und 30) raten: "))
# if guess == secret:
#     print("Gewonnen! Die Zahl ist " + str(secret))
# else:
#     print("Falsch. Die richtige Zahl war nicht " + str(guess))

# while schleife

secret = 16
guess = 0
while guess != secret: # (== ist ident, != ist nicht gleich)
    guess = int(input("Bitte Zahl (zwischen 1 und 30) raten: "))
    if guess == secret:
        print("Gewonnen! Die Zahl ist " + str(secret))
    else:
        print("Falsch. Die richtige Zahl war nicht " + str(guess))

