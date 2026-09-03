errors={}
dictionnary={}
with open("./data.txt","r") as file:
    for f in file:
        key,value=f.strip().split(" ",1)
        dictionnary[key.strip()]=value.strip()
        if errors.get(key.strip())==None:
            errors[key.strip()]=1
        else:
            errors[key.strip()]=errors[key.strip()]+1
print(errors)
print(dictionnary)

        

