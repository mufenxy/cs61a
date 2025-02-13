"""
def k_in_num(k,num):
    if num == 0:
        return k==0
    letter = []
    while num!=0:
        l = num%10
        letter.append(l)
        num=num//10
    return((k in letter))
"""
# 更简洁的版本

def k_in_num(k,num):
    return((str(k) in str(num)))

if __name__ == '__main__':
    print(k_in_num(1,123))
    print(k_in_num(5,123))
    print(k_in_num(0,0))