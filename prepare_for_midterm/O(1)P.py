# get the first element if it eamty return eamty
def get_first_element(list):
    if len(list) == 0:
        return"the list is empty"
    return list[0]
number = []
result = get_first_element(number)
print(result)