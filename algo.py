def sort_random(x):
    ones = []
    zeros = []
    sorted = [remove(x)]
    while len(x)>0:
        value = remove(x)
        if value != sorted[-1]:
            sorted+=[value]
        elif value == 0:
            zeros+=[value]
        else:
            ones+=[value]
    print(sorted)
    print(ones)
    print(zeros)
    if x:
        if sorted[-1]==0:
            while ones:
                sorted+=[remove(ones)]
                if zeros:
                     sorted+=[remove(zeros)]
    else:
        while zeros:
            sorted+=[remove(zeros)]
            if ones:
                sorted+=[remove(ones)]
    return sorted


def remove(alist):
    datum = alist[0]
    del alist[0]
    return datum

a = [1,0,0,1,0,0,1,1,0,1,0,1]
b = [0,0,0,0,1,1,1,1]

print(a)
b = sort_random(b)
print(b)
