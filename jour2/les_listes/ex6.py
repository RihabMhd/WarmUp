L = [10, 20, 30, 40, 50]
def chercheElement(element, liste):
    for i,v in enumerate(liste):
        if v==element:
            return i
    else:
        return False 
        
print(chercheElement(30,L))