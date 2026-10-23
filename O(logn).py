# write the program that seraching for the binary num in the list
list = [1,2,3,4,5,6,7,8,9,10]
target = 6
left = 0
right = len(list) -1
# find the mid number 
mid = left + right
while True:
    if mid[list] == target:
        print("have been found")
        break
    elif mid[list] < target:
        left = mid + 1
    else :
        right = mid - 1