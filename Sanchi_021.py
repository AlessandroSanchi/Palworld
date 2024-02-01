Products = ["laptop", "mouse", "keyboard"]
Prices = [1000, 50, 70]
Quantities = [5, 10, 8]
Input = 0

Zip = []



while True:
 if Input == 0:
   Input = int(input("Waiting input: "))  
   
   
      
 elif Input == 1:

  Zip = zip(Products,Prices,Quantities)
  print(list(Zip))
  Input = Input - 1

 
 elif Input == 2:
  product = input("Insert a product: ")
  price = float(input("Insert a price: "))
  quantity = int(input("Insert a quantity: "))
  Products.append(product)
  Prices.append(price)
  Quantities.append(quantity)
  Input = Input * 0


 elif Input == 3:
   ProductRemove = str(input("Choose the product to remove: "))
   if ProductRemove in Products:
    Index = Products.index(ProductRemove)
    Products.pop(Index)
    Prices.pop(Index)
    Quantities.pop(Index)
    Input = Input - 3
  
    
 elif Input == 4:
  print(Quantities)
  Input = Input - 4
     
 
  
 elif Input == 5:
   
  Input = Input -5
  
 elif Input == 6:
    break
     

