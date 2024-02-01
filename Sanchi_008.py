# ESERCIZIO 8
#Dato in input un numero n di pasticcini, dire quante scatole da 5 pezzi, da 3 pezzi e da 1 pezzo servono a contenerli. 
#Nota bene:
#- Utilizzare il minor numero di scatole possibili, non lasciando nessuna scatola parzialmente vuota.

Pasticcini = int(input("Inserire il numero di pasticcini: "))

Scatola5 = int(Pasticcini / 5)
Scatola5_resto = Pasticcini % 5

Scatola3 = int(Scatola5_resto / 3)
Scatola3_resto = Pasticcini % 3
Scatola1 = Scatola3_resto

print(f"Le scatole da 5 sono {Scatola5}")
print(f"Le scatole da 3 sono {Scatola3}")
print(f"Le scatole da 1 sono {Scatola1}")


  