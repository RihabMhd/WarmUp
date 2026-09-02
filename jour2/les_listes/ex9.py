chaine="Hello Rihab Mahdi Welcome to Youcode"
chaine2="Hello Rima Welcome to Youcode"
list1=chaine.split()
list2=chaine2.lower().split()


list_cleaned1=list(filter(lambda x: len(x)>3,list1))
list_cleaned2=list(filter(lambda x: len(x)>3,list2))
doublons=list(set(list_cleaned1) and set(list_cleaned2))
print(list1)
print(doublons)