def selectionSort(alist):

	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax = 0
		for location in range(1, fillslot+1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp

list_to_sort =[6,3,1,61,32,55,34,52,14,12,66,33,53]
selectionSort(list_to_sort)
print(list_to_sort)