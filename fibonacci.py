# Fibonacci numbers module (docs.python.org)

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__=='__main__':
    #Here we test only fib2!
    fib2_expected=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    res=fib2(40)

    error=False

    for exp, got in zip(fib2_expected, res):
        if exp!=got:
            print(f'Error: {exp}!={got}')
            error=True

