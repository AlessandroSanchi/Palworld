anno = int(input("Inserisci anno: "))

if anno <= 0 and anno >= 2100:
    print("non valido") 
    
    
if anno % 400 == 0:
    print("l' anno è bisestile")
    
elif anno % 4 == 0 and anno % 100 != 0:
 print("l'anno è bisestile") 
 
else:
    print("l'anno non è bisestile")
    

    
