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