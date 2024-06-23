def min_sum(arr):
    arr.sort()
    min_sum = 0
    for i in range(len(arr) // 2):
        min_sum += arr[i] * arr[len(arr)-1-i]
    return min_sum