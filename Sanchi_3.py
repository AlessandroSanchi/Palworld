Giorno = int(input("Inserire Giorno: "))
Mese = int(input("Inserire Mese: "))
Anno = int(input("Inserire Anno: "))

#Lista dei mesi
Gennaio = 31
Marzo = 31
Maggio = 31
Luglio = 31
Agosto = 31
Ottobre = 31
Dicembre = 31
Aprile = 30
Giugno = 30
Settembre = 30
Novembre = 30
Febbraio = 29

if Mese == 1:
    Mese = Gennaio
    
if  Mese == 2:
    Mese = Febbraio
    
if  Mese == 3:
    Mese = Marzo
    
if  Mese == 4:
    Mese = Aprile 
    
if  Mese == 5:
    Mese = Maggio
    
if  Mese == 6:
    Mese = Giugno
    
if  Mese == 7:
    Mese = Luglio

if  Mese == 8:
    Mese = Agosto
    
if  Mese == 9:
    Mese = Settembre
    
if  Mese == 10:
    Mese = Ottobre
    
if  Mese == 11:
    Mese = Novembre
    
if  Mese == 12:
    Mese = Dicembre
    
 #fine lista
    
   #controllo validità
    
if Giorno < 1 or Giorno > 31:
 print("Data non valida")

elif Anno < 0 or Anno > 2100:
 print("Data non valida")
 
elif Mese == 30 and Giorno == 31:
  print("Data non valida")
  
elif Mese == 29 and Anno % 400 != 0 or Mese == 29 and Anno % 4 != 0 and Anno % 100 != 1:
     print("Data non valida")  
     
 
else:
    print("Data Valida")

       

    

    
    
    

  
  
  


  

  
  