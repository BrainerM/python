def BinarySearch (arr, left, right, x):
    if right >= left:
            mid = (left + right) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return BinarySearch(arr, left, mid - 1, x)
            else: 
                return BinarySearch(arr, mid + 1, right, x)
    return -1