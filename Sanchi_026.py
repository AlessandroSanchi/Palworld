from math import sqrt

def my_input():
 a = int(input("a: "))
 b = int(input("b: "))
 c = int(input("c: "))
 return[a,b,c]

def elaborazione(a,b,c):
 delta = b * b - 4 * a * c
 if delta > 0:
  sol1 = (-b + sqrt(delta))/(2*a)
  sol2 = (-b - sqrt(delta))/(2*a)
 elif delta == 0:
  sol1 = -b /(2*a)
  sol2 = sol1
 elif delta < 0:
  sol1 = None
  sol2 = None


 return [sol1,sol2]


def risultati(x1,x2):
 print(f"X1 = {x1}")
 print(f"X2 = {x2}")
 


a,b,c = my_input()
soluzioni = elaborazione(a,b,c)
print(soluzioni)
 

 




    
