def two_of_three(i,j,k):
    """
    Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.
    """
    return(i*i+j*j+k*k-max(i,j,k)*max(i,j,k))

if __name__ == '__main__':
    print(two_of_three(1,2,3))
    print(two_of_three(5,3,1))
    print(two_of_three(10,2,8))
    print(two_of_three(5,5,5))