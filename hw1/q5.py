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
