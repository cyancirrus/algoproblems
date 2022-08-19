# Need find, append, search and replace in log(n) time - creation in O(nlogn)
# time expected : 10 minutes
# time spent    : 3 months back of mind 3 days * 3 hours of trying
# shrug         : u.u

from dataclasses import dataclass

@dataclass
class Sim:
    n:int
    value:str
    total:int=None

def max_heapify(a, index):
    left = (index + 1) * 2 - 1
    right = (index + 1) * 2
    largest=index
    if left < len(a) and a[index].n < a[left].n:
        a[left].total = a[left].n + a[index].n + (right < len(a) and a[right].n or 0)
        largest=left
    if right < len(a) and a[largest].n < a[right].n:
        a[right].total = a[right].n + a[left].n + a[index].n 
        largest=right
    if not largest == index:
        a[index],a[largest]=a[largest],a[index]
        max_heapify(a, largest)
    else:
        a[index].total=(
            (left < len(a) and a[left].total or 0) + 
            (right < len(a) and a[right].total or 0) +
            a[index].n
        )

def create_heap(a):
    for index in range(len(a) // 2 - 1,0 -1, -1):
        print(f"index:{index}")
        max_heapify(a, index)


# assume number
def sim(a, uniform:float):
    value = int(uniform*a[0].total)
    return find_value(a, value, 0)

def find_value(a, value, index):
    left = (index + 1) * 2 - 1
    right = (index + 1) * 2
    if value < a[index].n:
        return a[index]
    elif value := value - a[index].n <= a[left].total:
        return find_value(a, value, left)
    else:
        value = value - a[left].total
        return find_value(a,value,right)

def update_value(a, index, n):
    # need to come up with an update procedure, but it will be log n
    pass
    # a[index].n=n
    # return max_heapify(a, index) parent = index // 2


a=[Sim(1,"hello"), Sim(32, "there"), Sim(17, "world"), Sim(16, "!")]



create_heap(a)
print(a)

print(sim(a, 0.1))
print(sim(a, 0.99))
