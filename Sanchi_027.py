def valori() -> list[int]:
    n_valori = int(input("Inserici numero valori: "))
    valori = [] 
    while n_valori > 0:
         Valore = int(input("Inserisci valore: "))
         n_valori = n_valori - 1
         valori.append(Valore)
         print(valori)
    return valori



valori()



def is_pari():
     num = int(input("Inserisci numero: "))
     if num % 2 == 0:
          print(True)
     elif num % 2 != 0:
          print(False)

is_pari()

def lista():
     lista = []
     lista_pari = []
     n_valori = int(input("Inserici numero valori: "))
     while n_valori > 0:
      valore = int(input("Inserisci numero: "))
      n_valori = n_valori - 1
      lista.append(valore)
     for numero in lista:
         if numero % 2 == 0:
             numero = numero ** 2
             lista_pari.append(numero)
             somma = 0
     for num in lista_pari:
         somma += num
     print(somma)

lista()

