#find the target number
number = [34,35,4,646,63,435,3253]
found = False
taget = 63
for num in number:
    if num == taget:
        found = True
        break
print(found)