
import string
def ispangram(strg):
	alpha = set(string.ascii_lowercase)
	return set(strg.lower()) >= alpha

def check(l):
	new = str()
	for i in l:
		if ispangram(i):
			new +="0"
		else:
			new +="1"
	return new


lis = ["hsksscbdj", "jajhh", "The quick brown fox jumps over the lazy dog", "t"]
print(check(lis))

