def schedule(arrival, duration):
	finish = []
	for i in len(1,arrival):
		finish.append(arrival[i-1]+duration[i])
	print(finish)
	
