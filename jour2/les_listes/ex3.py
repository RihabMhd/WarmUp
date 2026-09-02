notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

print(notes)
moyenne=sum(notes)//len(notes)
print(moyenne)

max_notes_moyenne=list(filter(lambda n:(n>moyenne),notes))
print(max_notes_moyenne)

min_notes_moyenne=list(filter(lambda n:(n<moyenne),notes))
print(min_notes_moyenne)

max_note=max(notes)
print(max_note)

min_note=min(notes)
print(min_note)

note_sup_dix=len(list(filter(lambda n:(n>=10),notes)))
print(note_sup_dix)

per_reussite=round((note_sup_dix/len(notes))*100,2)
print(per_reussite)