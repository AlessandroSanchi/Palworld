Ore = int(input("Inserire numero di ore per la sosta: "))
Prezzo = 0
if Ore == 1:
 Prezzo = 1.5
   
    
if Ore <= 4:
    Prezzo = 1 * Ore
    
elif Ore > 4 and Ore <= 6:
 Prezzo = 0.5 * Ore
 
elif Ore > 6:
    Prezzo = 6
    
elif Ore > 24 or Ore < 0:
 print("Errore")


print(f"Il prezzo è di: {Prezzo}")

