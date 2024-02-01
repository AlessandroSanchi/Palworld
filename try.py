"""
1. Inizializza una lista di dizionari, ognuno rappresentante un dipendente con nome, ruolo e stipendio iniziale.
2. Stampa la lista di dipendenti.
3. Aggiungi un nuovo progetto alla tua azienda con un budget iniziale e costo orario per ora di lavoro su di esso.
4. Assegna a ciascun dipendente un impegno in ore su questo nuovo progetto, sottraendo dal budget del progetto il costo dei dipendenti per le ore svolte e sommando
 allo stipendio iniziale i compensi accessori per i progetti su cui ha lavorato.
5. Stampa la lista dei dipendenti con i relativi stipendi totali e le ore lavorate per ciascun progetto.
6. Stampa  le ore lavorate totali e il budget rimanente per ogni progetto.
"""

Lavoratore1 = {
    "Nome": "Bob",
    "Ruolo": "Portiere",
    "Stipendio": 104,
    "Ore totali": 0
}
Lavoratore2 = {
    "Nome": "Bob",
    "Ruolo": "Portiere",
    "Stipendio": 102,
    "Ore totali": 0
}
Lavoratore3 = {
    "Nome": "Bob",
    "Ruolo": "Portiere",
    "Stipendio": 106,
    "Ore totali": 0
}
#1
Azienda = [Lavoratore1,Lavoratore2,Lavoratore3]

Nome_Lavoratore = "Bobby"
Ruolo_Lavoratore = "Saldatore di saldavanai"
Stipendio_Lavoratore = 6


aggiungi_lavoratore = {"Nome": Nome_Lavoratore, "denominazione": Ruolo_Lavoratore, "metratura": Stipendio_Lavoratore}
Azienda.append(aggiungi_lavoratore)

#2
print(Azienda)

#3
Nuovo_progetto = {
   "Nome": "Sasso",
   "Budget": 1000000,
   "Costo all' ora": 15,

}
4#
Assegna_progetto = "Sasso"
Lavoratore_da_assegnare = Lavoratore1
Ore = 15
Ore_tot = 0

Ore_tot = Ore_tot + Ore
costo_per_ora = 8
costo_ore_tot = Ore * costo_per_ora
Budget = Budget_iniziale - costo_ore_tot
Lavoratore_da_assegnare["Stipendio"] = Lavoratore_da_assegnare["Stipendio"] + costo_ore_tot
Lavoratore_da_assegnare["Ore totali"] = Lavoratore_da_assegnare["Ore totali"] + Ore



#5-6
print(Azienda)
print(Ore_tot)
print(Budget)
