def fib1(n):
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b = b, a+b
    return result


def  fib2():
    print("Dummy function for testing module")
    return None
