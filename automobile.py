class Automobile:
    def __init__(self, codice, marca, modello, anno, posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.posti = posti
        self.noleggiata=False  #serve per capire se l'auto è già stata noleggiata o no. All'inizio è libera

    @property
    def anno(self,anno):        #metodo getter
        return self.anno       #restituisce l'attributo "anno"

    @anno.setter
    def anno(self,anno):       #metodo setter che imposta un valore all'anno
        if anno<1886:
            print("anno negativo")
            self._anno =1886    #assegna 1886 come anno minimo
        else:
            self.anno=anno

    @property
    def posti(self):        #di nuovo metodo getter, stavolta per il numero di posti
        return self.posti

    @posti.setter
    def posti(self,posti):
        if posti<0:
            print("posti negativo")
            self.posti=1             #1 è il valore minimo di posti
        else:
            self.posti=posti
    def __str__(self):
        if self.noleggiata:
            stato="Noleggiata"
        else:
            stato="Libera"
        return f"{self.codice}: {self.marca}, {self.modello}, {self.anno}, {self.posti} posti - {stato} - "