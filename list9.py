L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def maxmin():
    valeur_min = min(L)  
    valeur_max = max(L)  
    L[0] = valeur_min   
    return valeur_min, valeur_max   

min_val, max_val = maxmin()
print(f"-la valeur min est: {min_val}")
print(f"-la valeur max est: {max_val}")



