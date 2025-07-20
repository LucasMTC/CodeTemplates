def binarySearch(arr, num):
    l = 0
    r = len(arr) - 1
    while r >= l:
        mid = ((r - l) // 2) + l
        if arr[mid] > num:
            r = mid - 1
        elif arr[mid] < num:
            l = mid + 1
        else:
            return True
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binarySearch(arr, 1) == True
    assert binarySearch(arr, 10) == False