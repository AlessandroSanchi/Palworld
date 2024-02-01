"""
Esercizio 23 -_-

#FOCUS
liste di dizionari: imparare a combinare il precedente argomento (le liste) con i dizionari.
Realizzare un applicativo che permetta, mediante l'uso di dizionari e liste, la gestione del catalogo di un museo.
In particolare, l'applicativo dovrà permettere di:
1) Creare una nuova stanza (id, denominazione, metratura) 
2) Aggiungere un opera ad una stanza(titolo, artista, anno)
3) Consultare le opere presenti in una stanza
4) Consultare le stanze presenti
5) Cercare le informazioni su un opera
6) Cancellare un opera
7) Cancellare una stanza solo se vuota
 
"""


Museo = []


while True: 

 scelta = (input("inserisci un input: "))

 match scelta: 
  case '1': 
       id = (input("Inserire id stanza: "))
       Denominazione = str(input("Inserire denominazione: "))
       Metratura = int(input("Inserire Metratura: "))
       Aggiungi_stanza = {"id": id, "denominazione": Denominazione, "metratura": 25, "opere": []}
       Museo.append(Aggiungi_stanza)
       print(f"stanza creata: {Aggiungi_stanza}")
          
  case '2':
       ID_stanza = (input("Inserire id stanza: "))
       titolo_opera_da_aggiungere = str(input("Inserire titolo: "))
       Artista_opera_da_aggiungere = str(input("Inserire Artista: "))
       Anno_opera_da_aggiungere = int(input("Inserire anno: "))
       Opera_da_Aggiungere = {"titolo": titolo_opera_da_aggiungere, "artista": Artista_opera_da_aggiungere, "anno": Anno_opera_da_aggiungere}
       for stanza in Museo:
        if stanza["id"] == ID_stanza:
          stanza["opere"].append(Opera_da_Aggiungere)
          print(f"Opera aggiunta:  {stanza}")
       
          
  case '3':
               
       Id_stanza = (input("Inserire id stanza: "))

       for stanza in Museo:
        if stanza["id"] == Id_stanza:
          
          stanza_da_consultare = stanza
          opere_della_stanza = stanza["opere"]
          if opere_della_stanza == []:
              print("Stanza vuota")
          else:
           for opera in opere_della_stanza:
            
             print(f"titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")
        elif stanza["id"] != Id_stanza:
          print("Id non valido")
          break
           
       
          
 

  case '4':
      print("Stanze: ")
      for stanza in Museo:
       print(f"id: {stanza['id']}, denominazione: {stanza['denominazione']}, metratura: {stanza['metratura']}, opere: {stanza['opere']}")
      
      
        
  case '5':
    for stanza in Museo:
      ricerca_opera = str(input("Inserire opera: "))
      stanza_da_consultare = stanza
      opere_della_stanza = stanza_da_consultare["opere"]
      for opera in opere_della_stanza:
          if opera["titolo"] == ricerca_opera:
            print(f"Titolo: {opera['titolo']}, artista: {opera['artista']}, anno: {opera['anno']}")
            break

  case '6':
    Opera_da_cancellare = str(input("Inserire opera da cancellare: "))
    for stanza in Museo:
          opere_della_stanza = stanza["opere"]
          for opera in opere_della_stanza:
            if opera["titolo"] == Opera_da_cancellare:
             print("opera trovata...")
             opere_della_stanza.remove(opera)
             print("opera cancellata")
             break
            if not Opera_da_cancellare == opera["titolo"]:
              print("opera non trovata")
          break


        
  case '7':
    id_stanza_da_canc = (input("Inserire id stanza: "))
    
    for stanza in Museo:
      if stanza["id"] == id_stanza_da_canc:
         print("Stanza trovata...")

    if stanza["opere"] != []:
          print("stanza non vuota")
    else:
        Museo.remove(stanza)
        print("stanza cancellata")



  case '8':
    print("Leaving the museum....")
    break

      


      


        

