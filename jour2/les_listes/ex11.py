nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# une liste des carrés, une liste des nombres pairs, et une liste des nombres > 5.
list_carres=list(map(lambda x: x**2,nombres))
print(list_carres)
list_pairs=list(filter(lambda x: x%2==0,nombres))
print(list_pairs)
list_sup_5=list(filter(lambda x: x>5,nombres))
print(list_sup_5)