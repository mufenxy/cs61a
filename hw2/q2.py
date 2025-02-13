
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