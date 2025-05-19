from abc import ABC


class Personaggio:

    def __init__(self, nome: str, salute_massima: int):
        self.nome = nome
        self.salute_massima = salute_massima
        self.salute_attuale = salute_massima

    def __str__(self):
        return f"{self.nome} \n -HP: {self.salute_attuale}/{self.salute_massima}"


class PersonaggioNemico(Personaggio):

    def __init__(self, nome, salute_massima):
        super().__init__(nome, salute_massima)


class PersonaggioGiocatore(Personaggio):

    def __init__(self, nome, salute_massima):
        super().__init__(nome, salute_massima)
