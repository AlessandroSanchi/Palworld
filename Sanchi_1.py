Voto1 = int(input("Inserisci primo voto: "))
Voto2 = int(input("Inserisci secondo voto: "))
Voto3 = int(input("Inserisci terzo voto: "))
Voto4 = int(input("Inserisci quarto voto: "))
Voto5 = int(input("Inserisci quinto voto: "))

VotiValidi = 0
VotiSufficienti = 0


if Voto1 <= 10 and Voto1 >= 1:
 VotiValidi = VotiValidi+1

elif Voto1 >= 6:
 VotiSufficienti = VotiSufficienti + 1
if Voto2 <= 10 and Voto1 >= 1:
 VotiValidi = VotiValidi+1

elif Voto1 >= 6:
 VotiSufficienti = VotiSufficienti + 1

if Voto3 <= 10 and Voto1 >= 1:
 VotiValidi = VotiValidi + 1

elif Voto1 >= 6:
 VotiSufficienti = VotiSufficienti + 1

if Voto4 <= 10 and Voto1 >= 1:
 VotiValidi = VotiValidi + 1

elif Voto1 >= 6:
  VotiSufficienti = VotiSufficienti + 1

if Voto5 < 10 and Voto1 > 1:
  VotiValidi = VotiValidi + 1
 
elif Voto5 >= 6:
 VotiSufficienti = VotiSufficienti + 1


print(f"Voti Validi : {VotiValidi}")
print(f"Voti Sufficienti: {VotiSufficienti}")
