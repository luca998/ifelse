import math

a = input("Inserisci x alla seconda: ")
b = input("Inserisci x: ")
c = input("Inserisci c: ")

if a == 0 :
  print "L'equazione non e' di secondo grado"
  if b==0 and c==0:
    print "L'equazione e' indeterminata"
  elif b==0:
    print "L'equazione e' impossibile"
  elif c==0:
    print "L'incognita e' 0"
  else:
    x = -float(c)/float(b)
    print "L'incognita e': ", x
else:
  delta = (b*b) -4*a*c
  if delta > 0 : 
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print "Le soluzioni sono: ", x1, x2
  elif delta == 0 : 
    x = - float (b) / (2*float(a))
    print "L'equazione ha due soluzioni coincidenti: ", x
  elif delta < 0 :
    print "L'equazione non ammette soluzioni reali"


