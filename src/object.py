from abc import ABC


class Oggetto:

    def __init__(self, nome: str, descrizione: str, valore: int):
        self.nome = nome
        self.descrizione = descrizione
        self.valore = valore

    def __str__(self):
        return (
            f"{self.nome} \n -Descrizione: {self.descrizione} \n -valore:{self.valore}£"
        )


class Consumabili(Oggetto):

    def __init__(
        self, nome, descrizione, valore, effetti: str, modificatori: list, durata: int
    ):
        super().__init__(nome, descrizione, valore)
        self.effetti = effetti
        self.modificatori = modificatori
        modificatori = [0, 0, 0, 0, 0]
        self.durata = durata


class Equipaggiamento(Oggetto):

    def __init__(self, nome, descrizione, valore, modificatori: list):
        super().__init__(nome, descrizione, valore)
        self.modificatori = modificatori
        modificatori = [0, 0, 0, 0, 0]


class Arma(Equipaggiamento):

    def __init__(self, nome, descrizione, valore, modificatori, potenza: int, tipo: str):
        super().__init__(nome, descrizione, valore, modificatori)
        self.tipo = tipo
        self.potenza = potenza
        modificatori[1] = potenza
    def __str__(self):
        return (
            f"{self.nome} \n -{self.tipo} \n -Descrizione: {self.descrizione} \n -valore:{self.valore}£ \n -Potenza:{self.potenza}MP"
        ) 


class Armatura(Equipaggiamento):

    def __init__(self, nome, descrizione, valore, modificatori, armatura: int):
        super().__init__(nome, descrizione, valore, modificatori)
        self.armatura = armatura
        modificatori[2] = armatura


class Accessorio(Equipaggiamento):

    def __init__(
        self, nome, descrizione, valore, modificatori, effetto: str, effetti: list
    ):
        super().__init__(nome, descrizione, valore, modificatori)
        self.effetto = effetto
        self.effetti = effetti
        modificatori[0] = effetti[0]
        modificatori[1] = effetti[1]
        modificatori[2] = effetti[2]
        modificatori[3] = effetti[3]
        modificatori[4] = effetti[4]
