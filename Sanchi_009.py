#Dato in input il numero di secondi dire a quanti anni, mesi, giorni, ore, minuti e secondi corrispondono

Secondi = float(input("Inserire numero di secondi:"))

minuti = Secondi / 60
ore = minuti / 60
giorni = ore / 24
mesi = giorni / 30
anni = mesi / 12

print(f"minuti: {minuti}")
print(f"ore: {ore}")
print(f"giorni: {giorni}")
print(f"mesi: {mesi}")
print(f"anni: {anni}")
