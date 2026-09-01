chaine=input("Enter une chaine de character :")


# chaine_reversed="".join(reversed(chaine))
# print(chaine_reversed)

# print(chaine[::-1])


# def inverser_chaine(mot):
#     return mot[::-1]

# for i in range(len(chaine),0,-1):

chaine_reversed=""
for chn in chaine:
    chaine_reversed= chn + chaine_reversed

print(chaine_reversed)