list = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]


def filter(array):
    N = []
    for value in array :
        if value >=25 and value <= 90 :
            N.append(value)
    return N



filteredValue = filter(list)


print(filteredValue)

def product():
    result = 1
    for value in filteredValue:
        result = result * value
    return result

print(product())


