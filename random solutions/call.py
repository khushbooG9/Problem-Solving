from collections import defaultdict
def prioritycache(calllogs):
	sortcalllogs = sorted(calllogs, key = lambda x:x[0])
	print(sortcalllogs)
	main = {}
	cache = {}
	print(len(sortcalllogs))

	for k,v in calllogs:
		main[v]=0
	
	for i in range(len(sortcalllogs)):
		if sortcalllogs[i][1] not in main.keys():
			if sortcalllogs[i][1] not in cache.keys():
				main[sortcalllogs[i][1]]= 2
			else:
				cache[sortcalllogs[i][1]] = cache[sortcalllogs[i][1]] +2
		else:
			main[sortcalllogs[i][1]] = main[sortcalllogs[i][1]]+2
			if main[sortcalllogs[i][1]]>5:
				cache[sortcalllogs[i][1]] = main[sortcalllogs[i][1]]
				del main[sortcalllogs[i][1]] 
		removeids = []
		for k in cache.keys():
			print(k,"---------", sortcalllogs[i][1])
			if k!= sortcalllogs[i][1]:
				print(k,"---------", sortcalllogs[i][1])
				cache[sortcalllogs[i][1]] = cache[sortcalllogs[i][1]] - 1
				if cache[sortcalllogs[i][1]]<=3:
					main[sortcalllogs[i][1]] = cache[sortcalllogs[i][1]]
					removeids.append(k)
		for key in removeids:
			if key in cache.keys():
				del cache[key]

	return list(cache.keys())



log = [[1 , 1], [2,1], [3,1], [4,2], [5,2], [6,2]]
n = prioritycache(log)
print(n)
