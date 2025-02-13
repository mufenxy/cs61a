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
            