#1,2
Registro_voti = {     #Creato Registro dei voti
"Mario Gialli": 73,
"Luigi Barca": 32,
"Funky Bob": 89
}
#3
for Voti in Registro_voti.items(): #stampare il dizionario
 print(Voti)

#4
Registro_voti["Pontellini Kamill"] = 99 #Aggiunto uno studente
#5
for Voti in Registro_voti.items():  #stampare il dizionario
 print(Voti)

#6
Ricerca_studente = str(input("Inserisci studente: ")) #Quando l' imput è uguale al nome di uno studente, stampa il voto dello studente
for studenti in Registro_voti.keys():
 if studenti == Ricerca_studente:
    print("lo studente è nel registro")
    print(f"Voto {Ricerca_studente}: {Registro_voti[Ricerca_studente]}")

    




