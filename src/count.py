from abc import ABC


class contaturni:
    def __init(self):
        self.turno_corrente = 1

    def avanza_turno(self):
        self.turno_corrente += 1
        print(f"\n Turno {self.turno_corrente}")


def get_turno(self):
    return self.turno_corrente
