def fibonacci(term):
    if term <= 1:
        return term
    else:
        return (fibonacci(term-1)+fibonacci(term-2))

term = int(input("Enter the number of terms to generate Fibonacci series: "))
n = int(input("Enter the nth value: "))
if term <= 0:
    print("Enter valid term")
else:
    print("Fibonacci series:")
    fibo=[]
    for i in range(term):
        fibo.append(fibonacci(i))
    print("Fibonacci series: ",fibo)
    for i in range(len(fibo)):
        if i == n-1:
            print("The ",n,"value in fibonacci series is: ",fibo[i])

    