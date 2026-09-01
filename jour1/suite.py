# La suite de Syracuse (aussi appelée suite de Collatz ou conjecture de Syracuse) 
# est une suite définie pour un entier naturel positif n comme suit :

# Si n est pair, le terme suivant est n // 2.

# Si n est impair, le terme suivant est 3n + 1.

# La suite se termine lorsque n devient égal à 1.

# Écrire un code permettant de calculer cette suite


def syracuse(n):
    suite=[]
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        suite.append(n)
    return suite
print(syracuse(10))