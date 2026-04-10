#Oggetti

""" Esercizio pratico
Scrivi una classe Studente con attributi nome e corso, e un metodo
presentati() che stampa una frase di presentazione. """
""" class Studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

    def presentati(self):
        print(f"Mi chiamo {self.nome} e ho scelto il corso {self.corso}")

nome=str(input("Inserisci il tuo nome: "))
corso=str(input("Inserisci il corso: "))

studente_1=Studente(nome, corso)
studente_1.presentati() """
        
        
""" Crea una classe Persona con attributo "nome" e metodo
presentati().
Poi crea una sottoclasse Studente che aggiunge l'attributo "corso"
e lo include nella presentazione.
Infine, rendi l'attributo nome privato e permetti di leggerlo solo
tramite un metodo dedicato. """

""" class Persona:
    def __init__(self, nome):
        self.__nome= nome
        
    def get_nome(self):
        return self.__nome
       
    def presentati(self):
        print(f"Mi chiamo {self.__nome}")
    
      
class Studente(Persona):
    def __init__(self, nome, corso):
        super().__init__(nome)   # richiama il costruttore della classe madre
        self.corso = corso

    def presentati(self):
        print(f"Ciao, sono {self.get_nome()} e studio {self.corso}.")


nome=str(input("Inserisci il tuo nome: ")) 
identita=input("Sei uno studente? (s/n)").lower()

if identita == "s":
    corso = input("Inserisci il corso: ")
    persona_1 = Studente(nome, corso)
else:
    persona_1 = Persona(nome)

persona_1.presentati()
 """

""" Crea una classe Studente con:
Attributo di classe scuola = "Liceo Classico"
Attributo di istanza nome
Metodo di istanza presentati() che stampa "Sono X e
frequento Y"
Metodo di classe cambia_scuola(cls, nuova_scuola) che
modifica scuola per tutti gli studenti
     """
""" 
class Studente:
    scuola = "Liceo Classico"
    
    def __init__(self, nome):
        self.nome = nome
        
    def presentati(self):
        print(f"Sono {self.nome} e frequento {Studente.scuola}")
    
    @classmethod
    def cambia_scuola(cls, nuova_scuola):
        cls.scuola = nuova_scuola

    @classmethod
    def trova_studente(cls, nome_cercato):
        for studente in studenti:
            if studente.nome == nome_cercato:
                studente.presentati()
                return
        print("Studente non trovato")


studenti = []


def menu():
    print("*************** Archivio Studenti ****************")
    
    while True:
        print("\nScegli un'opzione:")
        print("1) Inserisci studente")
        print("2) Cerca studente")
        print("3) Cambia scuola")
        print("4) Esci")
        
        scelta = int(input("Scelta: "))
        
        if scelta == 1:
            studente_nome = input("Inserisci il nome dello studente: ")
            studente_1 = Studente(studente_nome)
            studenti.append(studente_1)
            studente_1.presentati()
            
        elif scelta == 2:
            studente_nome = input("Inserisci il nome dello studente da cercare: ")
            Studente.trova_studente(studente_nome)
            
        elif scelta == 3:
            nuova_scuola = input("Inserisci la nuova scuola: ")
            Studente.cambia_scuola(nuova_scuola)
            print("Scuola cambiata con successo!")
            
        elif scelta == 4:
            print("Uscita dal programma.")
            break


menu() """


""" Crea una classe Studente con attributi nome ed età.
Istanzia due studenti diversi e stampane i dati.
Aggiungi alla classe Studente un metodo presentati() che stampi un
messaggio con nome ed età.
Prova ad aggiungere un attributo "al volo" a uno studente, ad esempio
corso, e stampalo. """

""" class Studente:
    def __init__(self, nome, età):
        self.nome=nome
        self.età=età
        
    def presentati(self):
        print(f"Ciao sono {self.nome} ed ho {self.età}")
    
    @classmethod
    def trova_studente(cls, nome_cercato):
        for studente in studenti:
            if studente.nome == nome_cercato:
                studente.presentati()
                return studente
        print("Studente non trovato")
        return None

    
studenti=[]
    
def menu():
    
    print("*************Archivio***********")
       
    while True:
        
        print("Scegli una opzione: ")
        print("1) Aggiungi studente")
        print("2) Visualizza studente")
        print("3) Inserisci note")
        print("4) Esci dal programma")
        
        scelta=int(input("Digita numero opzione: "))
        
        if scelta == 1:
            nome_studente=input("Inserisci nome studente: ")
            eta_studente=input("Inserisci età studente: ")
            studente=Studente(nome_studente,eta_studente)
            studenti.append(studente)
        elif scelta==2:
            nome_studente=input("Inserisci nome studente: ")   
            Studente.trova_studente(nome_studente)
        elif scelta == 3:
            nome_studente = input("Inserisci nome studente: ")
            nota_studente = input("Inserisci nota per lo studente: ")

            studente = Studente.trova_studente(nome_studente)

            if studente is not None:
                studente.nota = nota_studente
                print(f"Nota aggiunta!")
                studente.presentati()
                print(f"Note: {studente.nota}")
        else:
            print("Uscita!")

menu()
             """
    # Crea una classe Libro con attributi titolo e autore.
# · Nel _init_, inizializza i valori
# · Nel_str_, restituisci una frase tipo: "Titolo: X, Autore: Y"

# Esempio:
# libro = Libro("1984", "George Orwell")
# print(libro)
# Output: Titolo: 1984, Autore: George Orwell

""" catalogo = {}  

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}"


def inserisci_libro(autore, titolo):
    libro = Libro(titolo, autore)
    catalogo[titolo] = libro
    print("Libro aggiunto!")


def elimina_libro(titolo):
    if titolo not in catalogo:
        print("Libro non trovato.")
        return

    libro = catalogo[titolo]
    print(libro)

    conferma = input(f"Sei sicuro di voler eliminare '{titolo}'? (s/n): ").lower()

    if conferma == "s":
        catalogo.pop(titolo)
        print("Libro eliminato con successo!")
    else:
        print("Nessuna operazione effettuata.")


def trova_libro():
    titolo = input("Inserisci titolo: ")
    if titolo not in catalogo:
        print("Libro non trovato.")
        return

    libro = catalogo[titolo]
    print(libro)


def mostra_catalogo():
    if not catalogo:
        print("Il catalogo è vuoto.")
        return

    print("Catalogo:")
    for titolo, libro in catalogo.items():
        print(f"- {libro}")


def menu():
    while True:
        print(
            "\nPremi: \n"
            "1. Per inserire un libro \n"
            "2. Per vedere i libri in catalogo \n"
            "3. Per eliminare un libro \n"
            "4. Per cercare un libro \n"
            "0. Per uscire"
        )

        scelta_input = input("Scelta: ")

        # per evitare crash se l'utente non inserisce un numero
        if not scelta_input.isdigit():
            print("Inserisci un numero valido!")
            continue

        scelta = int(scelta_input)

        if scelta == 1:
            autore = input("Inserisci un autore: ")
            titolo = input("Inserisci un titolo: ")
            inserisci_libro(autore, titolo)

        elif scelta == 2:
            mostra_catalogo()

        elif scelta == 3:
            titolo = input("Inserisci un titolo: ")
            elimina_libro(titolo)

        elif scelta == 4:
            trova_libro()

        elif scelta == 0:
            print("Uscita dal programma")
            break

        else:
            print("Inserisci una scelta valida!")


# Avvio del programma
menu() """

""" Crea una classe Automobile con:
· Variabile di classe ruote = 4
· Variabile di istanza modello
Crea due automobili con modelli diversi e stampa il numero di ruote e i modelli """

""" class Automobile:
    ruote= 4
    
    def __init__(self, modello):
        self.modello=modello
        
    def __str__(self):
        return f"Modello: {self.modello}, ruote: {self.ruote}"
    
auto1=Automobile("Panda")
auto2=Automobile("Tipo")

print(auto1)
print(auto2) """

""" Crea una classe ContoBancario con:
· Attributo privato __saldo
· Metodo deposita(importo) che aggiunge soldi solo se > 0
· Metodo preleva(importo) che riduce il saldo solo se sufficiente
Simula alcune operazioni di deposito e prelievo """

""" class ContoBancario:
    def __init__(self, saldo):
        self.__saldo= saldo
        
    def get_saldo(self):
        return self.__saldo
    
    def __str__(self):
        return f"{self.__saldo}"
  
    def deposita(self, importo):
        if importo>0:
            self.__saldo+=importo
            print("Operazione effettuata!")
        else:
            print("Devi inserire un importo di deposito positivo e maggiore di 0")
    
    def prelievo(self, importo):
        if importo>0 and self.__saldo>=importo:
            self.__saldo-=importo
            print("Operazione effettuata!")
        elif importo<=0:
            print("Devi inserire un importo di prelievo positivo e maggiore di 0")
        elif self.__saldo < importo:
            print(f"Non hai disponibilità sufficente, il tuo saldo è {self.get_saldo()}. \n"
                   "Ripetere con un altro importo")
        else:
            print("Hai eseguito un operazione non valida, verifica i dati")
            
def menu():
    print("**************** Banca v 1.0.0 **************")
    
    print("Benvenuto! Apri il tuo conto bancario ora! \n")
    somma=int(input("Quanto denaro vuoi inserire?"))
    conto=ContoBancario(somma)
    while True:
        scelta = int(input("Quale operazione vuoi fare? \n"
              "1. per verificare il saldo \n"
              "2. per effettuare prelievo \n"
              "3. per effettuare un versamento \n"
              "0. per uscire dal programma \n"))
        
        if scelta==1:
            print(conto)
            conto.get_saldo()
        elif scelta==2:
            importo=int(input("Quanto vuoi prelevare? \n"))
            conto.prelievo(importo)
        elif scelta==3:
            importo=int(input("Quanto vuoi versare? \n"))
            conto.deposita(importo)
        elif scelta==0:
            print("Uscita, a presto!")
            break
        else:
            print("Inserisci una scelta valida!")
            
menu() """

""" Crea una classe Animale con attributo nome e metodo verso().
Poi crea due classi derivate:
· Cane > verso() stampa "Bau"
· Gatto > verso() stampa "Miao"
Crea un oggetto di ciascuna classe e chiama il metodo verso().
Questo esercizio mostra chiaramente come ereditare e sovrascrivere i metodi. """

""" class Animale:
    def __init__(self, nome):
        self.nome= nome
    
    def __str__(self):
        return f"Sono un {self.nome}"
    def verso(self, suono):
        print(f"Sono un {self.nome} e faccio {suono}") 

class Cane(Animale):
    pass
    
class Gatto(Animale):
    pass
 
cane= Cane("Cane")
gatto=Gatto("Micio")

cane.verso("Bau")
gatto.verso("Miao") """

""" Crea una classe base Forma con metodo area().
Crea due classi derivate:
. Rettangolo > area = base * altezza
· Cerchio > area = Tt * r2
Crea una lista di forme e stampa l'area di ciascuna usando lo
stesso metodo area(). """

""" class Forma:
    def __init__(self):
        pass
    
    def area():
        pass
class Rettangolo(Forma):
    def __init__(self):
        super().__init__()
    
    def area(base, altezza):
        return base*altezza

class Cerchio(Forma):
    def __init__(self):
        super().__init__()
    def area(r2):
        return (3.14*r2)

r1=Rettangolo
c1=Cerchio

print(r1.area(10,2))
print(c1.area(25))
         """
         
         
""" Crea una classe astratta Veicolo con metodo astratto muovi().
Poi crea due classi concrete:
· Auto > muovi() stampa "L'auto si muove su strada"
· Aereo > muovi() stampa "L'aereo vola nel cielo"
Infine, scrivi una funzione che accetti un generico Veicolo e chiami muovi() """

""" from abc import ABC, abstractmethod 

class Veicolo(ABC):
    def muovi():
        pass
class Auto(Veicolo):
    def __init__(self):
        super().__init__()
    
    def muovi():
        print("L'auto si muove su strada")
class Aereo(Veicolo):
    def __init__(self):
        super().__init__()
    
    def muovi():
        print("L'aereo vola nel cielo")
        
def muovi_veicolo(Veicolo):
    Veicolo.muovi()
    
muovi_veicolo(Aereo)
muovi_veicolo(Auto) """



""" Crea una classe Studente che abbia:
. @classmethod per creare uno studente a partire da una stringa tipo "Luca-20-Matematica"
· @property per calcolare automaticamente l'anno di nascita a partire dall'età 
· @property con setter per impedire età negative """

""" from datetime import datetime

class Studente:
    def __init__(self, nome, eta, corso):
        self.nome = nome
        self._eta = eta
        self.corso = corso

    @classmethod
    def da_str(cls, stringa):
        nome, eta, corso = stringa.split("-")
        return cls(nome, int(eta), corso)

    @property
    def calcolo_anno(self):
        return datetime.now().year - self._eta

    @property
    def eta(self):
        return self._eta

    @eta.setter
    def eta(self, nuova_eta):
        if nuova_eta > 6:
            self._eta = nuova_eta
        else:
            print("Età non valida per uno studente")


s = Studente.da_str("Luca-20-Matematica")
print(s.calcolo_anno) """

""" Crea una classe Frazione che rappresenti una frazione con numeratore e denominatore.
Implementa i seguenti operatori:
· + (somma tra frazioni)
· == (uguaglianza tra frazioni, semplificando i valori)
._ str_ per stampare la frazione come "3/4" """

""" from math import gcd

def mcm(a, b):
    #Calcola il minimo comune multiplo di due numeri.
    return abs(a * b) // gcd(a, b)
class Frazione:
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore
        
    def __add__(self, altro_num, altro_den):
        if self.denominatore == altro_den:
            self.numeratore+=altro_num
        else:
            self.denominatore=mcm(self.denominatore,altro_den)
            self.numeratore=(self.numeratore*mcm(self.denominatore,altro_den)) + (altro_num*mcm(self.denominatore,altro_den)) 
            
    def __eq__(self, altro_num, altro_den):
        if self.denominatore == altro_den and self.numeratore == altro_num:
            return True
        else:
            n_mcm= mcm(self.denominatore,altro_den)
            nuovo_num_1 = self.numeratore / n_mcm
            nuovo_num_2 = altro_num / n_mcm
            nuovo_den_1 = self.denominatore / n_mcm
            nuovo_den_2 = altro_den / n_mcm
            if nuovo_num_1 == nuovo_num_2 and nuovo_den_1 == nuovo_den_2:
                return True
            else:
                return False
            
    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"
    
f1=Frazione(2,4)
f2=Frazione(1,2)
print(f1)
print(f1+f2)
print(f1==f2)
 """
""" from abc import ABC, abstractmethod 
class ContoBancario(ABC):
    def __init__(self, intestatario, saldo):
        self._saldo= saldo
        self._intestatario = intestatario
        
   
    @property
    def get_saldo(self):
        return self._saldo
    
    def __str__(self):
        return f"Conto di {self._intestatario} - Saldo: {self._saldo:.2f}$"
  
    @staticmethod
    def valida_importo(importo):
        if importo>0:
           return importo
        else:
           print("Devi inserire un importo di deposito positivo e maggiore di 0")
    
    @abstractmethod
    def deposita(self, importo):
        pass

    def prelievo(self, importo):
        pass

class ContoCorrente(ContoBancario):    
    COMMISSIONE = 1.5  
    def deposita(self, importo):
        if self.valida_importo(importo):
            self._saldo+=importo
            print("Operazione effettuata!")
        else:
            print("Importo non valido per il deposito!")
    
    
    def prelievo(self, importo):
        totale = importo + ContoCorrente.COMMISSIONE
        if self.valida_importo(importo) and self._saldo >= totale:
            self._saldo -= totale
            print("Operazione effettuata!")
        elif self._saldo < importo:
            print(f"Non hai disponibilità sufficente, il tuo saldo è {self.get_saldo()}. \n"
                   "Ripetere con un altro importo")
        else:
            print("Hai eseguito un operazione non valida, verifica i dati")
        
    def __add__(self, altro):
           nuovo_saldo = self._saldo + altro._saldo
           return ContoCorrente(f"{self._intestatario} & {altro._intestatario}", nuovo_saldo)
            
if __name__ == "__main__":
    cc1 = ContoCorrente("Luca", 1000)
    cc2 = ContoCorrente("Giulia", 500)
    

# Operazioni di base
cc1.deposita(200)
cc1.prelievo(50)
print(cc1)

# Fusione conti
conto_fuso = cc1 + cc2
print(conto_fuso) """
 
""" from abc import ABC, abstractmethod 
import math
class Forma(ABC):
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
    def __eq__(self, altra):
         return math.isclose(self.area(), altra.area())
    
    def __str__(self):
        return f"{self.__class__.__name__} - Area: {self.area():.2f}, Perimetro: {self.perimetro():.2f}"
    
class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    
    def perimetro(self):
        return 2 * (self.base + self.altezza)
    
    def area(self):
        return self.base * self.altezza
    
class Cerchio(Forma):
    def __init__(self, raggio):
        self._raggio = raggio
    
    @property
    def raggio(self):
        return self._raggio
    
    def diametro(self):
        return self._raggio * 2
    
    def area(self):
        return math.pi * self._raggio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self._raggio
    
class SommaFigure(Forma):
    def __init__(self, *figure):
        self.figure = figure
    
    def perimetro(self):
        return sum([f.perimetro() for f in self.figure])
    
    def area(self):
        return sum([f.area() for f in self.figure])
    
    def __str__(self):
        return f"SommaFigure - Area: {self.area():.2f}, Perimetro: {self.perimetro():.2f}"
    
Forma.__add__ = lambda self, altra: SommaFigure(self, altra)

rett= Rettangolo(4, 6)
cerchio = Cerchio(3)

print("=== Figure iniziali ===")
print(rett)
print(f"Diametro del cerchio: {cerchio.diametro()}")
print(cerchio)

print("\n=== Polimorfismo ===")
figure = [rett, cerchio]
for figura in figure:
    print(figura)

print("\n=== Confronto aree ===")
print(rett == cerchio)

print("\n=== Combinazione con + ===")
somma = rett + cerchio
print(somma)
         """
         
""" L'esercizio richiede di creare due classi:

Product: deve includere il nome e il prezzo, oltre a metodi speciali per la stampa e il confronto.
ShoppingCart: deve permettere di aggiungere/rimuovere prodotti, calcolare il totale e stampare il contenuto. 
Viene richiesto di implementare l'overloading degli operatori come la somma per unire i carrelli. """

""" Classe Product
I prodotti vengono istanziati e aggiunti a due carrelli.
Metodi speciali:
__str__: Rappresentazione leggibile del prodotto.
__eq__: Confronto tra prodotti per nome e prezzo. """

class Prodotto():
    def __init__(self, articolo, prezzo):
        self.articolo = articolo
        self.prezzo = prezzo
    
    def __str__(self):
        return f"{self.articolo} : {self.prezzo}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, articolo_confronto):
        if not isinstance(articolo_confronto, Prodotto): #isinstance serve a verificare che l'oggetto inserito sia della classe assegnata
            return False
        return self.articolo == articolo_confronto.articolo and self.prezzo == articolo_confronto.prezzo
    
""" Classe ShoppingCart
Costruttore: Inizializza una lista vuota di prodotti.
Metodi:
add_product: Aggiunge un prodotto al carrello.
remove_product: Rimuove un prodotto.
total_price: Calcola il totale dei prezzi dei prodotti.
__len__: Restituisce il numero dei prodotti.
__str__: Rappresentazione leggibile del carrello.
__add__: Unisce due carrelli creando un nuovo carrello  """
    
class Carrello():
    def __init__(self, *prodotti):
        self.prodotti = list(prodotti)
        
    def aggiungi_prodotto(self, prodotto):
        if not isinstance(prodotto, Prodotto):
            print("Devi aggiungere un prodotto")
        return self.prodotti.append(prodotto)
    
    def rimuovi_prodotto(self, prodotto):
        for prodotto in self.prodotti:
            self.prodotti.remove(prodotto)
    
    def prezzo_totale(self):
        somma = 0
        for p in self.prodotti:
            somma += p.prezzo
        return somma
   
    def __len__(self):
        return len(self.prodotti)
    
    def __str__(self):
        prodotti_str = ", ".join(str(p) for p in self.prodotti)
        return f"Prodotti nel carrello: {prodotti_str}, prezzo totale: {self.prezzo_totale()}"

    """ def __str__(self):
        return f'Prodotti nel carrello: {self.prodotti}, prezzo totale: {self.prezzo_totale()}' """
    
    def __add__(self, altro_carrello):
        return Carrello(*self.prodotti, *altro_carrello.prodotti)
    
    # Demo d’uso
if __name__ == "__main__":
    # creiamo alcuni prodotti
    penna = Prodotto("Penna", 1.50)
    quaderno = Prodotto("Quaderno", 2.30)
    zaino = Prodotto("Zaino", 25.00)

    # creiamo due carrelli
    cart1 = Carrello()
    cart2 = Carrello()

    # aggiungiamo prodotti
    cart1.aggiungi_prodotto(penna)
    cart1.aggiungi_prodotto(quaderno)
    cart2.aggiungi_prodotto(zaino)

    # stampiamo i carrelli
    print("=== Carrello 1 ===")
    print(cart1)
    print("\n=== Carrello 2 ===")
    print(cart2)

    # uniamo i carrelli con l'overloading di +
    merged = cart1 + cart2
    print("\n=== Carrello Unito ===")
    print(merged)

    # rimuoviamo un prodotto
    cart1.rimuovi_prodotto(penna)
    print("\n=== Carrello 1 dopo rimozione ===")
    print(cart1)

    # lunghezza totale
    print("\nNumero di articoli in merged:", len(merged))

    
