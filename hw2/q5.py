from operator import add,mul

def accumulate(merger, start, n, term):
    if n == 0:
        return start
    return merger(accumulate(merger, start, n - 1, term), term(n))

def identity(n):
    return(n)

def square(n):
    return(n*n)

if __name__=='__main__':
    print(accumulate(add, 0, 5, identity))
    print(accumulate(add, 11, 5, identity))
    print(accumulate(add, 11, 0, identity))
    print(accumulate(add, 11, 3, square))
    print(accumulate(mul, 2, 3, square))
    print(accumulate(lambda x, y: x + y + 1, 2, 3, square))
    print(accumulate(lambda x, y: 2 * x * y, 2, 3, square))
    print(accumulate(lambda x, y: (x + y) % 17, 19, 20, square))