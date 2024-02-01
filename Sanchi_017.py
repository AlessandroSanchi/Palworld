Valori = int(input("Inserisci Valori: "))
lista = []

for Numero in range(Valori):
    Numero = int(input("Inserisci un numero: "))
    lista.append(Numero)
    
Valore = int(input("inserire Valore per verificare la presenza: "))


if Valore in lista:
    print("il valore è nella lista")

else:
    print("il valore non c'è")
 