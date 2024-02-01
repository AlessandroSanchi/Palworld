
Decimale = int(input("Inserisci numero decimale:  "))
resto = 0
NumeroDecimale = []

while Decimale > 0:
    resto = (Decimale % 2) 
    if resto == 0 or resto == 1:
     NumeroDecimale.append(resto)
    Decimale = Decimale // 2

NumeroDecimale.reverse()
print(NumeroDecimale)






