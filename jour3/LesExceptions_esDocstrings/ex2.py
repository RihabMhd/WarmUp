list=[1, 2, 3, 4, 5]
list2=list(map(lambda x: x**2,list))
list2.append(64)
assert len(list)==len(list2),"Attention les 2 listes n'ont pas la même taille"