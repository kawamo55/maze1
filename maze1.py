import time as tm

dt=[
[0,1,2,3,4,5,6,7,8,9],
[1,'K','K','K','K','K','K','K','K','K'],
[2,'K','S','K',' ','K',' ',' ',' ','K'],
[3,'K',' ','K',' ','K',' ','K',' ','K'],
[4,'K',' ','K',' ','K',' ','K',' ','K'],
[5,'K',' ','K',' ','K',' ','K',' ','K'],
[6,'K',' ',' ',' ',' ',' ','K',' ','K'],
[7,'K','K','K','K','K',' ','K',' ','K'],
[8,'K',' ',' ',' ',' ',' ','K','G','K'],
[9,'K','K','K','K','K','K','K','K','K']
]

stackbf=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
stackpt=-1

def dispmaze(dt):
    for i in range(10):
        print(dt[i])

def getStart(dt):
    for y in range(10):
        for x in range(10):
            if dt[y][x]=='S':
                return(x,y)

def getNext(x,y):
    c=0
    rx, ry = (0,0)
#
    if dt[y-1][x]==' ' or dt[y-1][x]=='G':
        c += 1
        if (rx,ry)==(0,0):
            (ry,rx)=(y-1,x)
    if dt[y][x+1]==' ' or dt[y][x+1]=='G':
        c += 1
        if (ry,ry)==(0,0):
            (ry,rx)=(y,x+1)
    if dt[y+1][x]==' ' or dt[y+1][x]=='G':
        c += 1
        if (rx,ry)==(0,0):
            (ry,rx)=(y+1,x)
    if dt[y][x-1]==' ' or dt[y][x-1]=='G':
        c += 1
        if (rx,ry)==(0,0):
            (ry,rx)=(y,x-1)
#
    return (c,rx,ry)

def push_pos(x, y):
    global stackpt
    stackpt += 1
    stackbf[stackpt][0] = x
    stackbf[stackpt][1] = y

def pop_pos( ):
    global stackpt
    rx = stackbf[stackpt][0]
    ry = stackbf[stackpt][1]
    stackpt -= 1
    return(rx,ry)

dispmaze(dt)
x,y=getStart(dt)
c,x,y=getNext(x,y)
sx,sy=(0,0)

while dt[y][x] != 'G':
    if c > 1:
       push_pos(sx,sy)
    if c == 0:
       x, y = pop_pos()
    if dt[y][x]==' ':
        dt[y][x]='P'
    dispmaze(dt)
    sx,sy=(x,y)
    c,x,y = getNext(x,y)
    tm.sleep(2)

print("----- Goal -----")
