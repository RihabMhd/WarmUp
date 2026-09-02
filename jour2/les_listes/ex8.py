L = [7, 23, 5, 23, 7, 19, 23, 12, 29, 7, 5]
occurences={}
for i in range(len(L)):
    for j in range(i):
        if L[i]==L[j]:
            occurences[L[i]]=occurences.get(L[i],0)+1

    if occurences.get(L[i])==None:
        occurences[L[i]]=1
print(occurences)

            