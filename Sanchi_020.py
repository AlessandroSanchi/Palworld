print("1) View list")
print("2) Add item and quantity")
print("3) Edit item")
print("4) Remove item")
print("5) Esc")

i = 0
Lista = []
ListaQ = []
Zip = []
Input = 0

while True:
      
 if Input == 0 :
  print("#################################")
  Input = int(input("waiting input: "))
  print("#################################")
    
 elif Input == 1:
    print(list(Zip))
    Input = Input - 1
    
    
    
 elif Input == 2:
    NewItem = str(input("Insert a new Item: "))
    quantity = int(input("Insert quantity: "))
    Lista.append(NewItem)
    ListaQ.append(quantity)
    Zip = zip(Lista,ListaQ)

  
    
    Input = Input - 2
    
    
 elif Input == 3:
     EditItem = input("Choose the item  you want to edit: ")
     
    
     if EditItem in Lista:
         newItem = str(input("New Item: "))
         NewQuantity = int(input("New Quantity: "))
         Index = Lista.index(EditItem)
         Lista[Index] = newItem
         ListaQ[Index] = NewQuantity
         
         
         Input = Input - 3
         
     else:   
        
           Input = Input - 3
         
 elif Input == 4:
     RemoveItem = input("Choose the item to remove: ")
     if RemoveItem in Lista:
      index = Lista.index(RemoveItem)
      Lista.pop(index)
      ListaQ.pop(index)
      Input = Input - 4
      
     else:   
        
           Input = Input - 4
      
      
      
 elif Input == 5 :
    break
 
 elif Input > 5 or Input < 0 :
    print("Command not found.")
    Input = Input - Input
 
 
   
      
print("Leaving...")     
     
      
      
    
         
         
         
        
         
         
        
     
             
         
     
    













    


 
        
