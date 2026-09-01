age=int(input("Entrer votre age :"))

if age<18:
    print("l'entrée est refusée")
elif 18<age<25:
    print("l'entrée est gratuite")
elif age>25:
    print("l entrée est autorisée uniquement si elle est membre du club ou accompagnée d'un membre")


def club_permission(age):
    if age<18:
        print("l'entrée est refusée")
    elif 18<age<25:
        print("l'entrée est gratuite")
    elif age>25:
        print("l entrée est autorisée uniquement si elle est membre du club ou accompagnée d'un membre")