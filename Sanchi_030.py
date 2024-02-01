#Sulla base di quanto visto a lezione sul modulo random realizzare un programma che implementi il gioco della tombola o del bingo. 
#Al fine di far ciò, lo studente implementi le seguenti funzioni:
#1) def genera_cartella(id: int<str>)->dict:
#La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. Dare un id alla cartella.
#N.B.
#La cartella ha le seguenti caratteristiche:
#1) 3 righe e 9 colonne
#2) 15 numeri in totale (5 per riga)
#3) ogni colonna ha solo i numeri della decina di riferimento: la prima dall'1 al 10, la seconda dal 11 al 20....l'ultima dall'81 al 90
#
#
#2) def estrai_numero(numeri_estratti: list[])->int:
#La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, controllando che non sia duplicato, e restituisce tale numero come intero.
#
#3) def controlla_cartella(cartella: dict, numeri_estratti[])->list[bool]:
#Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella. Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
#es.
#[True, True, False, False, False] per una cartella che ha fatto terno(naturalmente per fare terno bisogna aver fatto anche ambo....)
#
#Realizzare un programma che implementi la logica di funzionamento:
#a) Utilizzando le opportune variabili di stato (es. una lista di cartelle, la lista dei numeri estratti, lo stato del gioco(ambo, terno,....))
#b) Utilizzando le funzioni precedentemente definite al fine di gestire le varie fasi del gioco.
import random


def genera_cartella(id: int)->dict:
   # shufflelata = [s for s in range(1,91)]
   # random.shuffle(shufflelata)
    riga1 = []
    riga2  = []
    riga3 = []
    colonna1 = [x for x in range(1, 10)]
    colonna2 = [x for x in range(10, 20)]
    colonna3 = [x for x in range(20, 30)]
    colonna4 = [x for x in range(30, 40)]
    colonna5 = [x for x in range(40, 50)]
    colonna6 = [x for x in range(50, 60)]
    colonna7 = [x for x in range(60, 70)] 
    colonna8 = [x for x in range(70, 80)] 
    colonna9 = [x for x in range(80, 91)]

    cf1 = []
    cf2 = []
    cf3 = []
    cf4 = []
    cf5 = []
    cf6 = []
    cf7 = []
    cf8 = []
    cf9 = []
    numeri_generati = []
    t = 0
 
    while t != 3:
        numero = random.choice(colonna1)
        colonna1.remove(numero)
        cf1.append(numero)
        

        numero = random.choice(colonna2)
        colonna2.remove(numero)
        cf2.append(numero)

        numero = random.choice(colonna3)
        colonna3.remove(numero)
        cf3.append(numero)

        numero = random.choice(colonna4)
        colonna4.remove(numero)
        cf4.append(numero)

        numero = random.choice(colonna5)
        colonna5.remove(numero)
        cf5.append(numero)

        numero = random.choice(colonna6)
        colonna6.remove(numero)
        cf6.append(numero)

        numero = random.choice(colonna7)
        colonna7.remove(numero)
        cf7.append(numero)

        numero = random.choice(colonna8)
        colonna8.remove(numero)
        cf8.append(numero)

        numero = random.choice(colonna9)
        colonna9.remove(numero)
        cf9.append(numero)
        t += 1   



    list.sort(cf1)
    list.sort(cf2)
    list.sort(cf3)
    list.sort(cf4)
    list.sort(cf5)
    list.sort(cf6)
    list.sort(cf7)    
    list.sort(cf8)    
    list.sort(cf9)
    list.sort(riga1)
    list.sort(riga2)
    list.sort(riga3)


    



    cartella = {"righe": [riga1,riga2,riga3], "colonne": [cf1,cf2,cf3,cf4,cf5,cf6,cf7,cf8,cf9]}



    return colonna1,colonna2,colonna3,colonna4,colonna5,colonna6,colonna7,colonna8,colonna9,cf1,cf2,cf3,cf4,cf5,cf6,cf7,cf8,cf9

genera_cartella(7)