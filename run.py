from src.player import PersonaggioGiocatore

p = PersonaggioGiocatore("pippo", 120)
print("Stampo il personaggio")
print(p)

from src.object import Arma

o = Arma( "Matteo", "Una possente arma", 20, [0,0,0,0,0], 20, "ascia")
print("stampo l'oggetto")
print(o)
