
def my_list(L):
    if len(L) > 0:  
        L[0], L[-1] = L[-1], L[0] 

L = [1, 2, 3, 4, 5]

print(L)
 
my_list(L)

print( L)
