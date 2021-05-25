def bubbleSort(alist):
	for passnum in range(len(alist)-1,0,-1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

list_to_sort =[6,3,1,61,32,55,34,52,14,12,66,33,53]
bubbleSort(list_to_sort)
print(list_to_sort)

def shortBubbleSort(alist):
	"""Modified to include parameter that check if listed is sorted early"""
	exchanges = True
	passnum = len(alist)-1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				exchanges = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		passnum = passnum - 1

list_to_sort =[6,3,1,61,32,55,34,52,14,12,66,33,53]
shortBubbleSort(list_to_sort)
print(list_to_sort)
