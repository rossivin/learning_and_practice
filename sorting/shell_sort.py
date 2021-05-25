def shellSort(alist):
	sub_list_count = len(alist)//2
	while sub_list_count > 0:
		for start_position in range(sub_list_count):
			gapInsertionSort(alist, start_position, sub_list_count)

		print("After increments of size", sub_list_count, "The list is:", alist)

		sub_list_count = sub_list_count // 2


def gapInsertionSort(alist, start, gap):
	for i in range(start+gap, len(alist), gap):
		current_value = alist[i]
		position = i

		while position > gap and alist[position-gap] > current_value:
			alist[position] = alist[position-gap]
			position = position - gap

		alist[position] = current_value

list_to_sort =[6,3,1,61,32,55,34,52,14,12,66,53]
shellSort(list_to_sort)
print(list_to_sort)