def count(n):
	p=1
	pos = []
	count = 0
	while(n>0):
		count = count + ( n & 1)
		if (n & 1)!=0:
			pos.append(p)
		p +=1
		n>>=1
	print(count)
	print(pos)
	print("_______________")


count(4)
count(2)
count(3)
count(7)
