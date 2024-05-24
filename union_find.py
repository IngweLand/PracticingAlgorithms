def union(i, j):
    internal_list:list
    first:list
    second:list
    for internal_list in l:
        if(i in internal_list):
            first = internal_list
            break
    for internal_list in l:
        if(j in internal_list):
            second = internal_list
            break
    if(first != second):
        first += second
        l.remove(second)
    
def union2(p:int, q:int):
    idp = l[p]
    idq = l[q]
    for idx, item in enumerate(l):
        if(item == idp):
            l[idx] = idq
    printl()

def create(j):
    for i in range(j):
        l.append([i])

def create2(j):
    global l
    l = [*range(j)]

def quick_union_get_root(p:int) -> int:
    while(p != l[p]):
        l[p] = l[l[p]]
        p = l[p]
    return p
    

def union_quick_union(p:int, q:int):
    proot = quick_union_get_root(p)
    qroot = quick_union_get_root(q)
    if(proot == qroot):
        return
    l[proot] = qroot

def is_connected_quick_union(p:int, q:int) -> bool:
    proot = quick_union_get_root(p)
    qroot = quick_union_get_root(q)
    return proot == qroot

def union_quick_union_weighted(p:int, q:int):
    proot = quick_union_get_root(p)
    qroot = quick_union_get_root(q)
    if(proot == qroot):
        return
    if(sizes[proot] < sizes[qroot]):
        l[proot] = qroot
        sizes[qroot] += sizes[proot]
    else:
        l[qroot] = proot
        sizes[proot] += sizes[qroot]

    

def printl():
    for idx, i in enumerate(l):
        print(f"{idx}: {i}")
    print()

l = []
sizes = [1]*10
create2(10)
print(l)

# union_quick_union(1,2)
# union_quick_union(3,4)
# union_quick_union(5,6)
# union_quick_union(7,8)
# union_quick_union(7,9)
# union_quick_union(2,8)
# union_quick_union(0,5)
# union_quick_union(1,9)
# print(is_connected_quick_union(3,6))
# print(is_connected_quick_union(7,9))
# print(is_connected_quick_union(1,4))
# print(is_connected_quick_union(1,7))

union_quick_union_weighted(4,3)
union_quick_union_weighted(3,8)
union_quick_union_weighted(6,5)
union_quick_union_weighted(9,4)
union_quick_union_weighted(2,1)
union_quick_union_weighted(5,0)
union_quick_union_weighted(7,2)
union_quick_union_weighted(6,1)
union_quick_union_weighted(7,3)


printl()

