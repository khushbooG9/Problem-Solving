def findend(i,j,a,output,index):
	x=len(a)
	y=len(a[0])
	flagc= 0
	flagr=0
	for m in range(i,x):
		if a[m][j]==1:
			flagr=1
			break
		if a[m][j]==5:
			pass
		for n in range(j,y):
			if a[m][n]==1:
				flagc=1
				break
			a[m][n]=5
	#print(m,n)
	if flagr==1: output[index].append(m-1)
	else: output[index].append(m)
	if flagc==1: output[index].append(n-1)
	else: output[index].append(n)

def rect(a):
	size=len(a)
	output=[]
	index=-1
	for i in range(size):
		for j in range(len(a[0])):
			if a[i][j]==0:
				output.append([i,j])
				index+=1
				findend(i,j,a,output,index)
	print(output)


m = [ 
  
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 0, 0, 0, 1], 
            [1, 0, 1, 0, 0, 0, 1], 
            [1, 0, 1, 1, 1, 1, 1], 
            [1, 0, 1, 0, 0, 0, 0], 
            [1, 1, 1, 0, 0, 0, 1], 
            [1, 1, 1, 1, 1, 1, 1] 
  
        ] 
rect(m)
