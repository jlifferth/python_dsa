# identify min and max values in array
# sum all values without each


def min_max_sum(arr):
    minVal = arr[0]
    maxVal = arr[0]

    # set min and max
    for value in arr:
        if value < minVal:
            minVal = value
        elif value > maxVal:
            maxVal = value
        else:
            pass

    minSum = 0
    maxSum = 0

    # create boolean tracker to determine whether a min or max value has already been used
    minUsed = False
    maxUsed = False

    # calculate min and max sums
    # min
    for value in arr:
        if not maxUsed:
            if value != maxVal:
                minSum += value
        if maxUsed:
            minSum += value
        if value == maxVal:
            maxUsed = True

    # max
    for value in arr:
        if not minUsed:
            if value != minVal:
                maxSum += value
        if minUsed:
            maxSum += value
        if value == minVal:
            minUsed = True

    print(minSum, maxSum)


array = [1, 2, 3, 4, 5]
array2 = [1, 3, 5, 7, 9]
array3 = [5, 5, 5, 5, 5]
min_max_sum(array)
