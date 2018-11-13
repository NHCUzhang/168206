def sum (alist):
	L=0
	L = int(L)
	if len(alist)==0:
		return 0
	else:
		L +=alist[0]
		alist.remove(alist[0])
		return L + sum(alist)

alist = [12,34,5]
s=sum(alist)
print(s)
