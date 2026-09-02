L = [10, 20, 30, 40, 50]
def chercheElement(element, liste):
    for i,v in enumerate(liste):
        if v==element:
            return i
    return False 
        
print(chercheElement(300,L)) 