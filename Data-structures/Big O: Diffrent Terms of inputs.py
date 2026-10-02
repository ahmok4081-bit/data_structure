def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
    #= O(2n) we drop the constand to n
def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
    #= it not O(2n) it O(a + b)
def print_items(a, b):
    for i in range(a):
        for j in range(b):
         print(i,j)

