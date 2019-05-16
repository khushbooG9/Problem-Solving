
from collections import defaultdict


def compare_file_lists(alpha_hash_list, bravo_hash_list):
	
	#Assuming alpha_hash_list is new version and bravo_hash_list is old 
	#Assuming alpha_hash_list[i] and bravo_hash_list[i] both refers to the ith file in the version
	changes = defaultdict(list)
	length = len(alpha_hash_list) if len(alpha_hash_list) <= len(bravo_hash_list) else len(bravo_hash_list)
	curidx = 0
	for i in range(length):
		if alpha_hash_list[i]==bravo_hash_list[i]:
			changes['unchanged'].append(alpha_hash_list[i])
		else:
			changes['added'].append(alpha_hash_list[i])
			changes['removed'].append(bravo_hash_list[i])
		curidx +=1

	# only more additions than removal
	if len(alpha_hash_list)>len(bravo_hash_list):
		while curidx<len(alpha_hash_list):
			changes['added'].append(alpha_hash_list[curidx])
			curidx+=1
	# more removals than addtion
	else : 
		while curidx<len(bravo_hash_list):
			changes['removed'].append(bravo_hash_list[curidx])
			curidx+=1

	

	### YOUR CODE HERE

	return changes


def add_change_type_flags_into_one_list(changes, change_type_list):
	
	new_list_with_flags = []
	
	
	for item in change_type_list:
		if item in changes.keys():
			for i in changes[item]:
				new_list_with_flags.append({'hash' : i, 'change_type' : item})
		else:
			new_list_with_flags.append({'hash' : "No file" + " " +str(item) , 'change_type' : item})
		





	return new_list_with_flags



def main(alpha_hash_list, bravo_hash_list, change_type_list):
	"""
	Runs comparison and combination, prints out results
	"""
	changes = compare_file_lists(alpha_hash_list, bravo_hash_list)

	combined_list = add_change_type_flags_into_one_list(changes, change_type_list)

	for item in combined_list:
		print(item)


	"""
	Example output

	{'hash': '813c9c630a770b91a829b072ae69b3582092a51d8406d5c3c18da1e3080f3452', 'change_type': 'added'}
	{'hash': '7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6', 'change_type': 'unchanged'}
	{'hash': 'f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0', 'change_type': 'unchanged'}
	{'hash': 'caccfde4071a22b06a5c7897c54cfe2d8812a254714882e80c7ff75aac6fa187', 'change_type': 'removed'}

	"""

a1 = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6", 
				   "f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0",
				   "813c9c630a770b91a829b072ae69b3582092a51d8406d5c3c18da1e3080f3452"]

b1 = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6", 
				   "f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0",
				   "caccfde4071a22b06a5c7897c54cfe2d8812a254714882e80c7ff75aac6fa187"]
a2 = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6", 
				   "f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0",
				   "813c9c630a770b91a829b072ae69b3582092a51d8406d5c3c18da1e3080f3452"]
b2 = []

a3 = []
b3 = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6", 
				   "f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0",
				   "caccfde4071a22b06a5c7897c54cfe2d8812a254714882e80c7ff75aac6fa187"]

a4 = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6", 
				   "813c9c630a770b91a829b072ae69b3582092a51d8406d5c3c18da1e3080f3452"]
b4 = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6"]
a5 = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6"]
b5 = ["7aec47f359bb75b768eeb95fa73b3a22d2fb053f6db3bb38daaff289512194c6", 
				   "f05e411f0e98d2ea40dcd2630d9e87a3587e61f44e28c9ab93925aa652c354f0"]
a6 = []
b6 = []

change_type_list = ["added", "unchanged", "removed"]
#Testing use cases
print("------------------1-----------------")
main(a1, b1, change_type_list)
print("------------------2-----------------")
main(a2, b2, change_type_list)
print("------------------3-----------------")
main(a3, b3, change_type_list)
print("------------------4-----------------")
main(a4, b4, change_type_list)
print("------------------5-----------------")
main(a5, b5, change_type_list)
print("------------------6-----------------")
main(a6, b6, change_type_list)
#print(compare_file_lists(alpha_hash_list, bravo_hash_list))
