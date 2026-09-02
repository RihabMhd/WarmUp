temperatures = [18, 25, 31, 14, 27, 35, 22, 19, 30, 12, 28]

list_temp_sup_25=[]
for i in range(len(temperatures)):
    if(temperatures[i]>25):
        list_temp_sup_25.append(temperatures[i])

print(list_temp_sup_25)

list_temp_inf_25=[]
for i in range(len(temperatures)):
    if(temperatures[i]<=25):
        list_temp_inf_25.append(temperatures[i])

print(list_temp_inf_25)

list_entre_20_30=[]
for i in range(len(temperatures)):
    if(20<=temperatures[i]<=30):
        list_entre_20_30.append(temperatures[i])
print(list_entre_20_30)

list_sup_30=[]
for i in range(len(temperatures)):
    if(20<=temperatures[i]<=30):
        list_sup_30.append(temperatures[i])
print(len(list_sup_30))

