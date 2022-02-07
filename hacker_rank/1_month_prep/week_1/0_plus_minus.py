

def plus_minus(arr):
    positive = 0
    negative = 0
    zero = 0
    length = len(arr)
    for value in arr:
        if value == 0:
            zero += 1
        elif value > 0:
            positive += 1
        elif value < 0:
            negative += 1
        else:
            print("Error with ", value)
    print("%.6f" % (positive / length))
    print("%.6f" % (negative / length))
    print("%.6f" % (zero / length))


array = [-4, 3, -9, 0, 4, 1]

plus_minus(array)
