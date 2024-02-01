#1
Studio_medico = {         #Creato Lo studio medico in un dizionario
"Dr_Boo": {
"Nome": "Simone Boo",
"Specializzazione": "Cardiologo",
"Pazienti": ["Franco","Toad"]
},
"Dr_Verdi":{
"Nome": "Bobby Verdi",
"Specializzazione": "Cardiologo",
"Pazienti": ["Simone","Antonio"]
}

}
#2
for dottori in Studio_medico.items(): #stampare il dizionario
    print(dottori)

#3

Studio_medico["Dr_Boo"]["Pazienti"] = ["Franco","Toad","Gilberto"]   #Aggiunto Gilberto ai pazienti del dottor Boo

#4
for studi in Studio_medico.items(): #stampare il dizionario
    print(studi)


