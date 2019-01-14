# your code goes here
def binary_search(arr, low, high, item):
    mid = (high + low) // 2

    if high >= low:
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return binary_search(arr, mid + 1, high, item)
        elif arr[mid] > item:
            return binary_search(arr, low, mid - 1, item)
    else:
        return -1

def main():
    arr = [2, 5, 7, 9, 10, 20, 25, 37, 56, 89]
    item = 25
    high  = len(arr) - 1
    print(binary_search(arr, 0, high, item))


main()