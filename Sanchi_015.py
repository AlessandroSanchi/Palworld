
Voti = int(input("inserisci voto/i: "))
i = 0
Somma  = 0
while Voti > 0:
    Voto = float(input("Inserisci voto: "))
    Somma += Voto
    i = i + 1
    Voti = Voti - 1
    
Media = Somma / i
print(Media)


    
    
    