def hillsnvalley(s):
	if not s:
		return 0
	if len(set(s))==1:
		return 1
	d = []
	for (x,y) in zip(s,s[1:]):
		if x!=y:
			d.append(y-x)
	count = 0
	for (a,b) in zip(d,d[1:]):
		if a*b<0:
			count +=1
	return 2+count


l1 = [2,3,4,5,3,3,8,8,0]
l2 = [0,0,0,0,0]
l3 = [1,2,1,2,1,2,1,2]
l4 = []

print("l1", hillsnvalley(l1))
print("l2", hillsnvalley(l2))
print("l3", hillsnvalley(l3))
print("l4", hillsnvalley(l4))



