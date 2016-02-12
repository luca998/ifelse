import math
solido = input("Calcolo del volume di un cubo o di una sfera.\n Scegli un solido 1 - Cubo, 2 - Sfera: ") 
if solido == 1 :
  lato = input ("Inserisci il lato: ")
  print "Il volume e': ", lato**3
elif solido == 2 :
  raggio = input ("Inserisci il raggio: ")
  print "Il volume della sfera e': ", (4.0/3.0*math.pi)*(raggio**3)


