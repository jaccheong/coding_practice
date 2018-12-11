def factorial(number):
    product = 1
    if number > 0:
        for i in range(number):
            product = (i+1) * product
    return product

print(factorial(input("number for factorial ")))
