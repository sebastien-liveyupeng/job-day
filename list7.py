L = [8, 24, 48, 2, 16]

def my_list(L):
    count = 0
    for nombre in L: 
        if nombre % 3 == 0:
            count += 1
    return count 

resultat = my_list(L)
print(resultat)
