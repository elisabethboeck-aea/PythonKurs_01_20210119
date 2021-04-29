#Über-Model/Parent-Model erstellen:
class Player():
    def __init__(self, first_name, last_name, height_cm, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight = weight

    # Funktion innerhalb des Models (=Methode, Methode sind functions innerhalb von Klassen)
    # gilt nur für objekte in einer Klasse
    def weight_to_lbs(self):
        pounds = self.weight * 2.29487534
        return pounds

#Erstellen einer Model-Klasse - gibt vor, welche Informationen jedes Object enthält:
class GolfPlayer(Player): # () holt die ersten vier Infos aus Player
    def __init__(self, first_name, last_name, height_cm, weight, points, handicap, tournaments):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight=weight) # super greift direkt auf die Parent-Klasse zu
        self.points = points
        self.handicap = handicap
        self.tournaments = tournaments
        # Ergänzen von Info aus einer Funktion:
        # self.pounds = self.weight_to_lbs()


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight, goals, red_cards, yellow_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight=weight)
        self.goals = goals
        self.red_cards = red_cards
        self.yellow_cards = yellow_cards

#Erstellen der Objekte, die zu dem Model gehören:
markus_golfobj = GolfPlayer(first_name="Markus", last_name="Angermann", height_cm=191, weight=89, points=50, handicap=32, tournaments=2)
petra_golfobj = GolfPlayer(first_name="Petra", last_name="Peterson", height_cm=165, weight=65, points=44, handicap=3, tournaments=40)
# print(markus_golfobj.handicap)
# print(petra_golfobj.last_name)
golf_players = [markus_golfobj, petra_golfobj]
for player in golf_players:
    print(player.last_name + " " + str(player.handicap))

print(petra_golfobj.weight_to_lbs())
# print(petra_golfobj.pounds)

ronaldo = FootballPlayer(first_name="Christiano", last_name="Ronaldo", height_cm=178, weight=80, goals=400, red_cards=20, yellow_cards=50)
print(ronaldo.red_cards)

#lesson 8 continued:
golf_players.sort(key=lambda x: x.height_cm, reverse=True) # reverse: true = aufsteigend/alphabetisch, false = andersrum
for player in golf_players:
    print("Sortiert:" + player.first_name)

#pypi.org: user können python packages, projects etc online stellen, die man nutzen kann
# wenn ein paket installiert wirde: unter settings > project: > interpreter einsehbar, welche enthalten sind

# wie geht das? -> im Terminal einfach den installationscode gemäß pypi eingeben (pip install prettytable), dann wird es herunter geladen