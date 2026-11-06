dic1 = {
    'value' : 11
}
dic2 = dic1
print('before the value update')
print(dic1, id(dic1))
print(dic2, id(dic2))

dic2['value'] = 22
print('after the value update')
print(dic1, id(dic1))
print(dic2, id(dic2))