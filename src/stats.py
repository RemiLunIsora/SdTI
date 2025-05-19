from abc import ABC


class Statistiche:

    def __init__(
        self,
        salute_massima: int,
        forza: int,
        difesa: int,
        velocità: int,
        fortuna: int,
        potenzaArma: int,
    ):
        self.salute_massima = salute_massima
        self.forza = forza
        self.difesa = difesa
        self.velocità = velocità
        self.fortuna = fortuna
        self.potenzaArma = potenzaArma
        self.danno = forza * potenzaArma
