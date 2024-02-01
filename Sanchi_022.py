Book = {
    "Title": "How to get Funky kong",
    "Author": "Nintendo",
    "Year_published": "2008",
    
    }

Book["Genre"] = "instructive"

Book["Year_published"] = "2009"

Book.pop("Author")

while True:
    Input = int(input("Inserisci input: "))
    if Input == 1:
     print(Book.keys())
    
     Input = Input * 0
     
     
    elif Input == 2:
      print(Book.values())
      Input = Input * 0
      
    elif Input == 3:
       print(Book.items())
       Input = Input * 0
      
    elif Input == 4:
     break