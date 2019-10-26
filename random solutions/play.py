def moveup(indexofq, l, k ):
	up = []
	for i in indexofq:
		if i>k:
			up.append((i-k)%l)
		else:
			up.append(l - (k-i)%l)
	return up

def movedown(indexofq, l, k):
	down= []
	for i in indexofq:
		if i>k:
			down.append(l-(i-k)%l)
		else:
			down.append((k-i)%l)
	return down


def playlist(songs, k, q):
    if (not songs) or (q not in songs):
        return -1
    indexofq = [i for i,v in enumerate(songs) if v==q ]
    print(indexofq)
    left = movedown(indexofq,len(songs),k)
    right = moveup(indexofq,len(songs),k)
    return min(min(left),min(right))





s = ["mks", "hihi","fd","sjdn","j","jj","hihi"]
ans = playlist(s, 4, "hihi")
print(ans)