def octal(num):
    oct=0
    c=1

    while num > 0:
        rem = num % 8
        oct += rem * c
        c *= 10
        num = num // 8
    return oct
    
num = int(input("Enter a number: "))
print("Octal form of number is: ",octal(num))

