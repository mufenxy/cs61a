## Q2

Write a function `k_in_num` which takes in two integers, `k` and `num`. `k_in_num` returns `True` if `num` has the digit `k` and returns `False` if `num` does not have the digit `k`. `0` is considered to have no digits.

## Q3

Python's operator module defines binary functions for Python's intrinsic arithmetic operators. For example, calling operator.add(2,3) is equivalent to calling the expression 2 + 3; both will return 5.

answer:

```python
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = operator.sub
    else:
        f = operator.add
    return f(a, b)
```

## Q4
Write a function that takes three positive numbers as arguments and returns the sum of the squares of the two smallest numbers. Use only a single line for the body of the function.

```python
def two_of_three(i,j,k):
    """
    Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.
    """
    return(i*i+j*j+k*k-max(i,j,k)*max(i,j,k))
```

## Q5
Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n

```python
def largest_factor(n):
    factor = n//2
    while factor>1:
        if n%factor==0:
            break
        else:
            factor-=1
    return factor

if __name__ == '__main__':
    print(largest_factor(15))
    print(largest_factor(80))
    print(largest_factor(13))
```

