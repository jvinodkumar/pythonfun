x=176
y=20

def SwapNum(x,y):
        print(x,y)
        x = x + y
        y = x - y
        x = x - y
        print(x,y)
        return [x,y]

SwapNum(x,y)