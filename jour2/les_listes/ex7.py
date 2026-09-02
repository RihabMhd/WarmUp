L = [7, 23, 5, 23, 7, 19, 23, 12, 29]
def compterOccurrences(element, liste):
    somme=0
    for i in range(len(liste)):
        if liste[i]==element:
            somme=somme+1
    return somme
print(compterOccurrences(23, L) )
print(compterOccurrences(7, L) )
print(compterOccurrences(100, L) )