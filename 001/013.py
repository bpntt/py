def quicksort(array):
    if len(array)<= 1:
        return array
    else:
        p = array[0]
    less = [i for i in array[1:] if i<=p]
    big = [i for i in array[1:] if i>p]
    return quicksort(less) + [p] + quicksort(big)
print(quicksort(input(" ").split()))