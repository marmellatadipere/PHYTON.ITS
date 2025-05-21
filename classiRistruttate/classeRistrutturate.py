from enum import Enum
import re
from datetime import date

#CLASSI DEI TIPI DI DATO
class Indirizzo:
    def __init__(self, via:str, civico:str, cap:int):
        self.via = via
        self.setCivico(civico)
        self.setCap(cap)

    def setCivico(self, civico:int) -> None:
        if not re.fullmatch(r'\d+[A-za-z]$', civico):
            raise ValueError("Inserire almeno un numero e al massimo una lettera")
        self.civico = civico
    def setCap(self, cap: int) -> None:
        if not isinstance(cap, int) or not re.fullmatch(r'\d{5}', str(cap)):
            raise ValueError("Il CAP deve essere composto esattamente da 5 cifre.")
        self.cap = cap
    
    def __str__(self):
        return f"Indirizzo {self.via} {self.civico} - {self.cap}"
    
    def __hash__(self)->int:
        return hash( (self.via(), self.civico()) )
    def __eq__(self, other)->bool:
        if other is None or \
        not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        return (self.via(), self.civico() ) == (other.via(), other.civico())

class CodiceFiscale:
    cfRegex = r"^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$"

    def __init__(self, codice: str):
        codice = codice.upper()
        if not re.fullmatch(self.cfRegex, codice):
            raise ValueError("Codice Fiscale non valido.")
        self.codice = codice

    def __str__(self) -> str:
        return f"Codice fiscale: {self.codice}"
    
    
class Stato(Enum):
    inPreparazione = "in preparazione"
    inviato = "inviato"
    daInviare = "da inviare"
    saldato = "saldato"


class PartitaIva:
    def __init__(self, piva: str):
        self.set_piva(piva)

    def set_piva(self, piva: str) -> None:
        if not re.match(r'^\d{11}$', piva):
            raise ValueError("La Partita IVA deve contenere esattamente 11 cifre.")
        self.piva = piva

    def __str__(self):
        return f"Partita IVA: {self.piva}"


#CLASSI RISTRUTURATE

class Citta:
    def __init__(self,nome:str):
        self.nome = nome
    
    def __str__(self):
        return f"Nome della città: {self.nome}"
    
class Regione:
    def __init__(self,nome:str):
        self.nome = nome
    
    def __str__(self):
        return f"Nome della Regione: {self.nome}" 

class Nazione:
    def __init__(self,nome:str):
        self.nome = nome
    
    def __str__(self):
        return f"Nome della Nazione: {self.nome}"

class Direttore:
    def __init__(self, nome:str, cognome:str, codicefiscale:CodiceFiscale, dataNascita:date, anniServizio:float):
        self.nome = nome
        self.cognome = cognome
        self.codicefiscale = codicefiscale
        self.dataNascita = dataNascita
        self.anniServizio = anniServizio
    
    def __str__(self):
        return f"Nome: {self.nome}/nCognome: {self.cognome}\nCodice Fiscale: {self.codicefiscale}\nData di nascita: {self.dataNascita}\nAnni di servizio: {self.anniServizio}"
    
class Dipartimento:
    def __init__(self, nome:str, indirizzo:Indirizzo):
        self.nome = nome
        self.indirizzo = indirizzo

class Ordine:
    def __init__(self, dataStipula:date, imponibile: float, iva: PartitaIva, descrizione: str, stato:Stato):
        self.dataStipula = dataStipula
        self.imponibile = imponibile
        self.iva = iva
        self.descrizione = descrizione
        self.stato = stato

