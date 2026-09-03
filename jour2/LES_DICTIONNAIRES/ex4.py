notes_etudiants = {"Omar": 15, "Sara": 8, "Yassine": 17, 
                   "Imane": 11, "Hamza": 6, "Nadia": 14}

# list_values=notes_etudiants.values()
# notes_sup_10=list(filter(lambda x: x>=10,list_values))
# notes_inf_10=list(filter(lambda x:x<10,list_values))
# print(notes_inf_10)
# print(notes_sup_10)


# notes={'note_inf_10':[],'note_sup_10':[]}
# for k,v in notes_etudiants.items():
#         print(k,v)
#         if v<10:
#             notes['note_inf_10']=notes['note_inf_10']+[{"name":k,"note":v}]
#         else :
#             notes['note_sup_10']=notes['note_sup_10']+[{"name":k,"note":v}]
# print(notes)



per_reussite=round(sum(notes_etudiants.values())/len(notes_etudiants))
print(per_reussite)

meilleur_etd=max(notes_etudiants.values())
print(meilleur_etd)