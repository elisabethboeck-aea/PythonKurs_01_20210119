import random # importiert fertige funktionen/bibliotheken
import json
import datetime

#current_time = datetime.datetime.now() # gibt das heutige datum mit jetziger Uhrzeit aus
# print(current_time)

secret = random.randint(1, 30)
attempts = 0

with open("lesson5_game-score-dict.txt","r") as score_file:
    score_list = json.loads(score_file.read())
   # score_list.sort() # sortiert die Ergebnisse der Größe nach # geht nichtmehr, da der json string nicht sortiert werden kann
   # print("Top scores:" + str(score_list[:1]))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " Versuche, Datum: " + score_dict.get("date")) # scrote_dict["date"] greift auf element mit index date zu, score_dict.get("date") macht das selbe

while True:
    guess = int(input("Bitte Zahl (zwischen 1 und 30) raten: "))
    attempts += 1 # ident mit attempts = attempts + 1
    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
        with open("lesson5_game-score-dict.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Gewonnen! Die Zahl ist " + str(secret))
        print("Versuche: " + str(attempts))
        break
    elif guess > secret:
        print("Falsch, die gesuchte Zahl ist kleiner.")
    elif guess < secret:
        print("Falsch, die gesuchte Zahl ist größer.")