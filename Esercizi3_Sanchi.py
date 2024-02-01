#1

Attività_giornaliere = {     #inizializzate le attività settimanali

"Lunedì":["Corsa"],
"Martedì":["Lezione di matematica"],
"Mercoledì":["Allenamento"],
"Giovedì":["Italiano", "Storia"],
"Venerdì":["Inglese"],
"Sabato":[],
"Domenica":["Falegnameria"]

}

#2
for attivita in Attività_giornaliere.items(): #stampare il dizionario
    print(attivita)



#3
Attività_giornaliere["Sabato"] = ["Escursione"] #Aggiunto "Escursione" nelle attività del sabato


        


#4
for attivita in Attività_giornaliere.items(): #stampare il dizionario aggiornato
  print(attivita)