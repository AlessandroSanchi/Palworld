Numero = float(input("Inserisci numero"))


if Numero <= 28000:
 Numero = Numero * 0.23 + Numero
 
elif Numero > 28000 and Numero < 50000:
    Numero = (Numero - 28000) * 0.35 + Numero * 0.23
    
#non finito