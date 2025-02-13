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
