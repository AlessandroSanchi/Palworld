#Dati in input il voto in trentesimi e il numero di crediti di tre esami, calcolare la media ponderata
#Nota bene
#Fare il controllo che il voto sia da 1 a 30 e che i crediti siano da 1 a 12
print("INSERIRE I VOTI IN TRENTESIMI")
Voto1 = float(input("Inserire primo voto: "))
Crediti1 = int(input("Inserire crediti: "))

Voto2 = float(input("Inserire secondo voto: "))
Crediti2 = int(input("Inserire crediti: "))

Voto3 = float(input("Inserire terzo voto: "))
Crediti3 = int(input("Inserire crediti: "))

CreditiTot = Crediti1+Crediti2+Crediti3

Voto1t = Voto1 * Crediti1
Voto2t = Voto2 * Crediti2
Voto3t = Voto3 * Crediti3
VotoTot = Voto1t + Voto2t + Voto3t 

Media = VotoTot / CreditiTot
print(Media)
