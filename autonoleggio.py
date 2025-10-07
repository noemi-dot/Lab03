class Automobile:
    def __init__(self, codice, marca, modello, anno, posti):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.posti = posti

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.responsabile=responsabile
        self.automobili=[]   #le caricheremo dal file automobili.csv


    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    dati=line.strip().split(",")
                    codice = dati[0]
                    marca = dati[1]
                    modello = dati[2]
                    anno = int(dati[3])
                    posti = int(dati[4]) if dati[4] else 0
                    auto = Automobile(codice, marca, modello, anno, posti)
                    self.automobili.append(auto)
        except FileNotFoundError:
            print("File non trovato")

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO
