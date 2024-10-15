def cube (number):
    return number*number*number

def by_three (number):
    if number %3 ==0:
        return cube(number)
    else:
        return False

d = int(input("Please Enter a Number = "))
print("Cube is =", by_three (d))