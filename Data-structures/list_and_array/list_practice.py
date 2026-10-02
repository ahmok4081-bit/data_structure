def even_squares(numbers: list[int]) -> list[int]:
    
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i**2)
    return result
numbers = [1,2,3,4,5,6]
print(even_squares(numbers))
            

    