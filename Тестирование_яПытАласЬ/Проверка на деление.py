def divide(x, y):
    assert y != 0 , "Can't be divisible by 0."
    return round(x/y, 2)

z = divide(81,9)
print(z)

a = divide(33,0)
print(a)
