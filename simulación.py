import random

def simulator(n):
  z = True
  s = 0
  lose = 0
  win = 0

  while z: 
  
      eleccion = random.randint(0, 2)
  
      puertas = ["p1","p2","p3"]
      carro = random.randint(0, 2)
      puertas[carro] = "carro"
    
      if eleccion != puertas.index("carro"):
        s += 1
        if n == 1:
          win += 1
        elif n == 0:
          lose += 1
          
      elif eleccion == puertas.index("carro") :
        s += 1
        if n == 1:
          lose += 1
        elif n == 0:
          win += 1
        
      if s == 200: 
          z = False
  return(print(win/s))
     
# 1 = switch
simulator(1)

# 0 = no switch
simulator(0)
