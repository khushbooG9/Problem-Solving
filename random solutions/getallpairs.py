def getallpairs(a, k):
	d = {}
	l=[]
	
	for i in range(len(a)):
		if (a[i])in d.keys():
			l.append((a[i], d[a[i]]))
		else:
			d[k-a[i]]=a[i]

	print(l)

d = [2, 3, 4, -2, 6, 8, 9, 11 ]
getallpairs(d,6)