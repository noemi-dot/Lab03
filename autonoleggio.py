
import csv
from automobile import Automobile
from noleggio import Noleggio

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.responsabile=responsabile
        self.automobili=[]   #le caricheremo dal file automobili.csv. questa è una lista di oggetti
        self.noleggi=[]


    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader=csv.reader(file)

                righe=[riga for riga in reader]
                for line in righe:
                    codice = line[0]
                    marca = line[1]
                    modello = line[2]
                    anno = int(line[3])
                    posti = int(line[4])
                    auto = Automobile(codice, marca, modello, anno, posti)
                    self.automobili.append(auto)
                return self.automobili

        except FileNotFoundError:
            print("File non trovato")
            return None

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        if self.automobili: #se ci sono
            for a in self.automobili:
                ultimo_codice=max(a.codice[1:])  #considera solo la parte numerica, togliendo la A
                nuovo_codice=f"A{ultimo_codice}+1"   #aggiunge 1 al codice più grande del file
        else:
            nuovo_codice="A1"

        nuova_automobile = Automobile(nuovo_codice,marca, modello, anno, num_posti)
        self.automobili.append(nuova_automobile)
        return nuova_automobile


    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        alias_automobili=self.automobili[:]
        for i in range(len(alias_automobili)-1):
            for j in range(i+1, len(alias_automobili)):
                if alias_automobili[i].marca > alias_automobili[j].marca:
                    alias_automobili[i],alias_automobili[j] = alias_automobili[j],alias_automobili[i] #scambia le due auto

        return alias_automobili


    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        a=None
        for auto in self.automobili:
            if auto.codice== id_automobile:
                a=auto
                break

        if auto == None:
            raise Exception("l'auto non esiste")
        if auto.noleggiata:
            raise Exception("l'auto è già stata noleggiata")

        if self.noleggi:  # se ci sono già noleggi
            for n in self.noleggi:
            # prendo tutti gli ID esistenti e estraggo la parte numerica
                ultimo_numero = max(n.id_noleggio[1:])  #cosi toglie la N e considera solo la parte numerica
                id_noleggio = f"N{ultimo_numero + 1}"
        else:
            # se non ci sono ancora noleggi, parto da N1
            id_noleggio = "N1"
        auto.noleggiata=True

        noleggio = Noleggio(data, id_noleggio, id_automobile, cognome_cliente)
        self.noleggi.append(noleggio)

        return self.noleggi

    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        noleggio_terminato=None

        for noleggio in self.noleggi:
            if noleggio.id_noleggio == id_noleggio:
                noleggio_terminato=noleggio
                break
        if noleggio_terminato is None:
            raise Exception("il noleggio non esiste")

        for a in self.automobili:
            if a.codice == noleggio_terminato.id_automobile:
                a.noleggiata=False
                break
        self.noleggi.remove(noleggio_terminato)
        return noleggio_terminato

