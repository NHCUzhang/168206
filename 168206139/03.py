def MergeSort(alist):
    if len(alist) <= 1:
        return alist
    middle = len(alist) // 2
    left = MergeSort(alist[:middle])
    right = MergeSort(alist[middle:])
    return merge(left, right)

def merge(a,b):
    c = []
    d = e = 0
    while d < len(a) and e < len(b):
        if a[d] < b[e]:
            c.append(a[d])
            d += 1
        else:
            c.append(b[e])
            e += 1
    if d == len(a):
        for i in b[e:]:
            c.append(i)
    else:
        for i in a[d:]:
            c.append(i)
    return c

list = [8,5,4,1,3,9,7]
print(MergeSort(list))
