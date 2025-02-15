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