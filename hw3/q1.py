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