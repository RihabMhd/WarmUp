notes = {"Python": 15, "SQL": 13, "JavaScript": 17, "Git": 14, "Linux": 12}

notes.keys()
notes.values()

for k,v in notes.items():
    print(k,':',v)

moy=sum(notes.values())//len(notes)
print(moy)

max=max(notes.values())
min=min(notes.values())