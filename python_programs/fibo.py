def fibonacci(term):
    if term <= 1:
        return term
    else:
        return (fibonacci(term-1)+fibonacci(term-2))

term = int(input("Enter the number of terms to generate Fibonacci series: "))

if term <= 0:
    print("Enter valid term")
else:
    print("Fibonacci series:")
    for i in range(term):
        print(fibonacci(i))