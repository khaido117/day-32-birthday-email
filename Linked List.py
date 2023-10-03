myList = None
for i in range(5, 0, -1):  # Reverse the range to start from 5 and go down to 1
    if myList is None:
        myList = [i, None]
    else:
        cur = [i, myList]
        myList = cur
cur = None