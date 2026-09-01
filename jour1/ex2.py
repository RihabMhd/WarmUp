nom=input("Enter votre nom :")
salaire_horaire=float(input("Enter votre salaire horaire :"))
heure_travailler=float(input("Enter les heures que vous avez travailler :"))

if heure_travailler>40:
    heures_seplementaire=heure_travailler-40
    demi_salaire=salaire_horaire*40
    salaire_total=demi_salaire+heures_seplementaire*salaire_horaire*1.5
else :
    salaire_total=salaire_horaire*heure_travailler

print(f"Employe : {nom} \n Salaire est :{salaire_total}")


def salary_calculator(nom, salaire_horaire, heure_travailler):
    if heure_travailler>40:
        heures_seplementaire=heure_travailler-40
        demi_salaire=salaire_horaire*40
        salaire_total=demi_salaire+heures_seplementaire*salaire_horaire*1.5
    else :
        salaire_total=salaire_horaire*heure_travailler

    print(f"Employe : {nom} \n Salaire est :{salaire_total}")