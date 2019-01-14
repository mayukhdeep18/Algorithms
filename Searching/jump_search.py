def jump_search(arr,size,item):
    prev = 0
    jump = pow(size,0.5)

    while arr[int(jump)] <= item:
        if arr[int(jump)] == item:
            return int(jump)
        prev = int(jump)
        jump += pow(size,0.5)

        if prev >= size:
            return -1

    for i in range(prev,int(jump)):
        if arr[i] == item:
            return i

    return -1

def main():
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    item = 38
    size = len(arr)-1
    print(jump_search(arr,size,item))

main()