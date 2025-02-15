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