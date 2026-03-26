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