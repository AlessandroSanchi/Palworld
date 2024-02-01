"""
Scrivere una funzione che passati come parametro la classe ambientale (euro 0, euro1,...., euro6), 
i kW e gli anni passati dall'immatricolazione di un autoveicolo, calcoli il bollo auto e l'eventuale superbollo.
 Nel caso non sia previsto il superbollo si scelga se restituire 0 oppure None. Utilizzare la funzione in un programma di esempio.

N.B.
Creare una funzione specifica per il superbollo da usare nella funzione principale.
es.
def calcola_superbollo (kW:int, immatricolazione: int) ->float: ....

Signature metodo principale:
def calcola_bollo (classe_ambientale:int, kW:int, immatricolazione:int) ->list[float] | None: ....
N.B.
La funzione può eseguire un controllo sui dati inseriti in ingresso e in caso di dati non validi (es. negativi) restituisce None


utilizzo:
bollo, superbollo = calcola_bollo (.......................................

Calcolo bollo:
Euro 0 fino a 100 kW pagano 3 euro a kW e 4,50 euro per ogni kW oltre i 100
Euro 1 fino a 100 kW pagano 2,9 euro a kW e 4,35 euro per ogni kW oltre i 100
Euro 2 fino a 100 kW pagano 2,8 euro a kW e 4,20 euro per ogni kW oltre i 100
Euro 3 fino a 100 kW pagano 2,7 euro a kW e 4,05 euro per ogni kW oltre i 100
Euro 4 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Euro 5 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Euro 6 fino a 100 kW pagano 2,58 euro a kW e 3,87 euro per ogni kW oltre i 100
Calcolo superbollo:
Auto nuove e fino a 5 anni pagano 20 euro per ogni kW oltre i 185
Dopo i primi 5 anni pagano 12 euro per ogni kW oltre i 185
Dopo i 10 anni pagano 6 euro per ogni kW oltre i 185
Dopo i 15 anni pagano 3 euro per ogni kW oltre i 185
Dopo i 20 anni non pagano il superbollo
"""

def sasso():
   Kw = 186
   eta = 12
   Classe = "Euro0"
   return Kw,eta,Classe

def calcolo_sasso(Kw:float,Classe:str):
   if Classe == 'Euro0' and Kw <= 100:
    bollo = Kw * 3
    bolloFinale = bollo
    return bolloFinale   
    
   elif Kw > 100 and Classe == 'Euro0' :
     resto = Kw - 100
     bollo = 100 * 3
     bollo2 = resto * 4.5
     bolloFinale = bollo + bollo2
     return bolloFinale
   
   if Classe == 'Euro1' and Kw <= 100:
    bollo = Kw * 2.9
    bolloFinale = bollo
    return bolloFinale   
    
   elif Kw > 100 and Classe == 'Euro1' :
     resto = Kw - 100
     bollo = 100 * 2.9
     bollo2 = resto * 4.35
     bolloFinale = bollo + bollo2
     return bolloFinale 
   
   if Classe == 'Euro2' and Kw <= 100:
    bollo = Kw * 2.8
    bolloFinale = bollo
    return bolloFinale   
    
   elif Kw > 100 and Classe == 'Euro2' :
     resto = Kw - 100
     bollo = 100 * 2.8
     bollo2 = resto * 4.20
     bolloFinale = bollo + bollo2
     return bolloFinale
   
   if Classe == 'Euro3' and Kw <= 100:
    bollo = Kw * 2.7
    bolloFinale = bollo
    return bolloFinale   
    
   elif Kw > 100 and Classe == 'Euro3' :
     resto = Kw - 100
     bollo = 100 * 2.7
     bollo2 = resto * 4.05
     bolloFinale = bollo + bollo2
     return bolloFinale
    
   if Classe == 'Euro4' and Kw <= 100:
    bollo = Kw * 2.58
    bolloFinale = bollo
    return bolloFinale   
    
   elif Kw > 100 and Classe == 'Euro4' :
     resto = Kw - 100
     bollo = 100 * 2.58
     bollo2 = resto * 3.87
     bolloFinale = bollo + bollo2
     return bolloFinale
    
   if Classe == 'Euro5' and Kw <= 100:
    bollo = Kw * 2.58
    bolloFinale = bollo
    return bolloFinale   
    
   elif Kw > 100 and Classe == 'Euro5':
     resto = Kw - 100
     bollo = 100 * 2.58
     bollo2 = resto * 3.87
     bolloFinale = bollo + bollo2
     return bolloFinale    

   if Classe == 'Euro6' and Kw <= 100:
    bollo = Kw * 2.58
    bolloFinale = bollo
    return bolloFinale   
    
   elif Kw > 100 and Classe == 'Euro6':
     resto = Kw - 100
     bollo = 100 * 2.58
     bollo2 = resto * 3.87
     bolloFinale = bollo + bollo2
     return bolloFinale
   

   
Kw,eta,Classe = sasso()
bollo = calcolo_sasso(Kw,Classe)

if not bollo:
  print('Error Bollo')
else:
  print(f"Il bollo da pagare ammonta a: {bollo}€ (Classe: {Classe}, Kw totali: {Kw})")

def calcola_supersasso(kW : int ,eta : int):
  if eta <= 5 and kW > 185:
    resto = kW - 185
    supersasso = resto * 12
    return supersasso

  if eta > 5 and kW > 185 and eta <= 10:
    resto = kW - 185
    supersasso = resto * 12
    return supersasso

  if eta > 10 and kW > 185 and eta <= 15:
    resto = kW - 185
    supersasso = resto * 6
    return supersasso

  if eta > 15 and kW > 185 and eta <= 20:
    resto = kW - 185
    supersasso = resto * 3
    return supersasso

  if eta > 20 and kW > 185:
    resto = kW - 185
    supersasso = resto * 0
    return supersasso



superbollo = calcola_supersasso(Kw,eta)
if not superbollo:
  print('Superbollo: 0')
else:
 print(f"Il Superbollo da pagare ammonta a: {superbollo}€ (Età: {eta}, Kw totali: {Kw})")

