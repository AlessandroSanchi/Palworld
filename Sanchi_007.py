#Dati in input 3 numeri, mostrare il maggiore

Numero1 = int(input("Inserire un numero: "))
Numero2 = int(input("Inserire un numero: "))
Numero3 = int(input("Inserire un numero: "))

if Numero1 > Numero2 and Numero1 > Numero3:
    print("Il primo numero e' maggiore")
    
elif Numero2 > Numero1 and Numero2 > Numero3:
    print("Il secondo numero e' maggiore")
    
elif Numero3 > Numero1 and Numero3 >  Numero2:
    print("Il terzo numero e' maggiore")
    
else:
    print("ERROR")
    
