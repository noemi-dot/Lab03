class Noleggio:
    def __init__(self, data, id_noleggio, id_automobile, cognome_cliente):
        self.data = data
        self.id_noleggio = id_noleggio
        self.id_automobile = id_automobile
        self.cognome_cliente = cognome_cliente


    def __repr__(self):
        return f"{self.id_noleggio}: Auto {self.id_automobile}, Cliente {self.cognome_cliente}, Data {self.data}"