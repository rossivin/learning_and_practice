#If item is present, best case is 1 search, worst case is n search, and average case is O(n/2)
#If item is not present, average case is O(n)

def sequentialSearch(alist, item):
	pos = 0
	found = False

	while pos < len(alist) and not found:
		if alist[pos] == item:
			found = True
		else:
			pos = pos + 1

	return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

#Only change is if item is not present, average case is now n/2

def orderedSequentialSearch(alist, item):
	pos = 0
	found = False
	stop = False

	while pos < len(alist) and not found and not stop:
		if alist[pos] == item:
			found = True
		else:
			if alist[pos] > item:
				stop = True
			else:
				pos = pos + 1

	return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))