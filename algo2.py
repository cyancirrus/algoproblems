def sort_random(x):
    compliment = []
    sorted = [remove(x)]
    while len(x)>0:
        value = remove(x)
        if value != sorted[-1]:
            sorted+=[value]
            if compliment:
                sorted+=[remove(compliment)]
        else:
            compliment+=[value]
    return sorted


def remove(alist):
    datum = alist[0]
    del alist[0]
    return datum

a = [1,0,0,1,0,0,1,1,0,1,0,1]
b = [0,0,0,0,1,1,1,1]

print(a)
b = sort_random(a)
print(b)
