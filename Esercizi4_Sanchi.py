#1

Mario = {                         #inizializzati contatti che vengono messi nella lista "Contatti"
"Nome": "Mario",
"Cognome": "Azzurri",
"Numero di telefono": 1299964333
}

Toad = {
"Nome": "Toad",
"Cognome": "Verdi",
"Numero di telefono": 13443434223
}

Larry = {
  "Nome": "Larry",
"Cognome": "Blu",
"Numero di telefono": 137994423
}

Contatti = [Mario,Toad,Larry]

#2
for contatto in Contatti:  #stampare la lista
    print(contatto)

#3
nuovo_contatto = {        #creato un nuovo contatto e aggiunto alla lista "Contatti"
"Nome": "Kamill",
"Cognome": "Berlini",
"Numero di telefono": 1254678863
}
Contatti.append(nuovo_contatto)  


#4
nome_numero_da_cambiare = str(input("Inserire Nome: ")) #Se viene inserito il nome e il cognome di un contatto, il numero di telefono può essere modificato
cognome_numero_da_cambiare = str(input("Inserire Cognome: "))
for rubrica in Contatti:
    if rubrica["Nome"] == nome_numero_da_cambiare and rubrica["Cognome"] == cognome_numero_da_cambiare:
      rubrica["Numero di telefono"] = int(input("Inserire nuovo numero di telefono: "))



#5
for rubrica in Contatti: #stampare la lista
    print(rubrica)