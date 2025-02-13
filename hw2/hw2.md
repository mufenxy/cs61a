## Q1
Implement the function count_until_larger. count_until_larger takes in a positive integer num. count_until_larger counts the distance between the rightmost digit of num and the nearest greater digit; to do so, the function counts digits from right to left. Once it encounters a digit larger than the rightmost digit, it returns that count. If no such digit exists, then the function returns -1.

```python
def count_until_larger(num):
    letter = []
    while num!=0:
        letter.append(num%10)
        num=num//10
    j=1
    while j<len(letter):
        if letter[j]>letter[0]:
            return j
        j = j+1
    return -1

if __name__=='__main__':
    print(count_until_larger(8117))
```

## Q2

Write a function filter_sequence which takes in two integers, start and stop, as well as a function cond, which takes in a single argument and outputs a boolean value. filter_sequence returns the sum of all digits from start to stop (inclusive) for which cond returns True.

```python
def filter_sequence(cond,start,stop):
    total = start
    while start<stop:
        start+=1
        if cond(start):
            total+=start
    return total

if __name__ == '__main__':
    print(filter_sequence(lambda x: x % 2 == 0, 0, 10))
    print(filter_sequence(lambda x: x % 2 == 1, 0, 10))

```

## Q3

Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

Pick a positive integer n as the start.
If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
Continue this process until n is 1.
The number n will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

This sequence of values of n is often called a Hailstone sequence. Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:

```python
def hailstone(n,j=1):
    print(n)
    if n==1:
        return(j)
    else:
        if n%2==0:
            n=n//2
        else:
            n=n*3+1
        return(hailstone(n,j+1)) #递归调用的结果必须return回去

if __name__ == '__main__':
    a = hailstone(1)
    print(f"a={a}")
```

## Q4

The summation(n, term) function from the higher-order functions lecture adds up term(1) + ... + term(n). Write a similar function called product that returns term(1) * ... * term(n).

```python
def product(n,term):
    if n==1:
        return(term(1))
    else:
        return(term(n)*product(n-1,term))
```

## Q5

实现累积函数：
>def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    "*** YOUR CODE HERE ***"

```python
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
```