class Automobile:
    def __init__(self, codice, marca, modello, anno, posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.posti = posti
        self.noleggiata=False  #serve per capire se l'auto è già stata noleggiata o no. All'inizio è libera

    def __str__(self):
        if self.noleggiata:
            stato="Noleggiata"
        else:
            stato="Libera"
        return f"{self.codice}: {self.marca}, {self.modello}, {self.anno}, {self.posti} posti - {stato} - "