## Q1

Implement the function neighbor_digits. neighbor_digits takes in a positive integer num and an optional argument prev_digit. neighbor_digits outputs the number of digits in num that have the same digit to its right or left.

```python
def neighbor_digits(num):
    count = 0
    digit_str = str(num)
    for i in range(len(digit_str)):
        if (i > 0 and digit_str[i] == digit_str[i - 1]) or (i < len(digit_str) - 1 and digit_str[i] == digit_str[i + 1]):
            count += 1
    return count


if __name__=='__main__':
    print(neighbor_digits(111))
    print(neighbor_digits(123))
    print(neighbor_digits(1122))
    print(neighbor_digits(112))
```


## Q2

Implement the function has_subseq, which takes in a number n and a "sequence" of digits seq. The function returns whether n contains seq as a subsequence, which does not have to be consecutive.

```python
def has_subseq(n,seq):
    n_str = str(n)
    seq_str = str(seq)
    if len(n_str) < len(seq_str):
        return False
    seq_set = 0
    for char in seq_str:
        if char == n_str[seq_set]:
            seq_set+=1
            if seq_set == len(seq_str):
                return True
    return False

if __name__=='__main__':
    print(has_subseq(123, 12))
    print(has_subseq(141, 11))
    print(has_subseq(144, 12))
    print(has_subseq(144, 1441))
    print(has_subseq(1343412, 134))
```

## Q3

Write a recursive function num_eights that takes a positive integer pos and returns the number of times the digit 8 appears in pos.

```python
def num_eights(pos):
    if pos == 0:
        return 0
    else:
        return (1 if pos%10==8 else 0)+num_eights(pos//10)

    
if __name__=='__main__':
    print(num_eights(3))
    print(num_eights(8))
    print(num_eights(88888888))
    print(num_eights(2638))
    print(num_eights(86380))
    print(num_eights(12345))
```

## Q4


The ping-pong sequence counts up starting from 1 and is always either counting up or counting down. At element k, the direction switches if k is a multiple of 8 or contains the digit 8. The first 30 elements of the ping-pong sequence are listed below, with direction swaps marked using brackets at the 8th, 16th, 18th, 24th, and 28th elements:

```python
def num_eight(num):
    return (True if (num%8==0 or str(8) in str(num)) else False)

def pingpong(order,direction=1,current=1):
    if order==1:
        return (current if direction==1 else -current)  #注意如果直接返回current不能保证order[1]时的方向
    if num_eight(order-1):
        direction = -direction
    return(pingpong(order-1,direction,current+direction))

if __name__ == '__main__':
    for i in [8,10,15,21,22,30,68,69,80,81,82,100]:
        print(pingpong(i))
```

## Q5

Given a positive integer change, a set of coins makes change for change if the sum of the values of the coins is change

```python
def get_larger_coin(coin):
    return {1:5,5:10,10:25}.get(coin,None)

def count_coins(change,coin=1):
    if change==0:
        return 1
    if change<0 or coin is None:
        return 0
    return count_coins(change-coin,coin)+count_coins(change,get_larger_coin(coin))


if __name__ == '__main__':
    for i in [15,10,20,100,200]:
        print(f"<<<count_coins({i}")
        print(count_coins(i))
```