donnees = ["Omar", 25, "Casabdonneesanca", 15.5, True]
occurences={}

# for d in donnees:
#     print(type(d))
list_numbers=[]
for i in range(len(donnees)):
    for j in range(i):
        if type(donnees[i])==type(donnees[j]):
            occurences[type(donnees[i])]=occurences.get(type(donnees[i]),0)+1

    if occurences.get(type(donnees[i]))==None:
        occurences[type(donnees[i])]=1

    if occurences.get(type(donnees[i])) == type(10):
        list_numbers.append(donnees[i])
print(occurences)

print(list_numbers)