def insertionSort(alist):
	for index in range(1, len(alist)):

		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position-1] > currentvalue:
			alist[position] = alist[position-1]
			position = position-1

		alist[position] = currentvalue

list_to_sort =[6,3,1,61,32,55,34,52,14,12,66,33,53]
insertionSort(list_to_sort)
print(list_to_sort)