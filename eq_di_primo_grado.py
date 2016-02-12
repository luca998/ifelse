a=input("Inserisci x:")
b=input("Inserisci b:")
if a==0 and b==0:
    print "L'equazione e' indeterminata"
elif a==0:
    print "L'equazione e' impossibile"
elif b==0:
    print "L'incognita e' uguale a 0"
else:
    x = float (-b)/(a)
    print "L'equazione ammette come soluzione il valore:", x
