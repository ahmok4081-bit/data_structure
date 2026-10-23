
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
#15/2

target = 13

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Found:", numbers[mid])
        break
    elif numbers[mid] < target:
       left = mid + 1
    else:
       right = mid - 1
