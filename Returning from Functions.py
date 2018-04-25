def max(x, y):
    if x >= y:
        return x
    else:
        return y

print(max(4, 7))
z = max(8, 5)
print(z)

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")
print(add_numbers(4, 5))