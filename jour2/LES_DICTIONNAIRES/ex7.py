from functools import reduce
etudiants = [
    {"nom": "Omar", "age": 22, "note": 15},
    {"nom": "Sara", "age": 21, "note": 17},
    {"nom": "Yassine", "age": 23, "note": 9},
    {"nom": "Imane", "age": 20, "note": 13},
    {"nom": "Hamza", "age": 24, "note": 7}
]

etds_admis=list(filter(lambda x : x["note"]>10,etudiants))
print(etds_admis)
length=len(etudiants)
les_notes=list(map(lambda x:x["note"],etudiants))
moyenne=reduce(lambda x , y: x+y//length,les_notes)
print(moyenne)
max=etudiants[0]["note"]

etd_excellent=[x for x in etudiants if x["note"] > max]
print(etd_excellent)