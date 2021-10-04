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

def isWay(c):
    rb = False
    for wc in [' ','1','2','3','4']:
        if wc==c:
            rb=True
            break
    return rb

def getNext(d,x,y,wx,wy):
    if (wx,wy)==(0,0):
        if dt[y-1][x]==' ' and dt[y][x+1]=='K':
            d=1
            wx,wy=(x+1,y)
        elif dt[y][x+1]==' ' and dt[y+1][x]=='K':
            d=2
            wx,wy=(x,y+1)
        elif dt[y+1][x]==' ' and dt[y][x-1]=='K':
            d=3
            wx,wy=(x-1,y)
        elif dt[y][x+1]==' ' and dt[y-1][x]=='K':
            d=4
            wx,wy=(x,y-1)
    else:
        if isWay(dt[y-1][x]) and dt[y-1][x+1]==' ':
            d=12
        elif isWay(dt[y][x+1]) and dt[y+1][x+1]==' ':
            d=23
        elif isWay(dt[y+1][x]) and dt[y+1][x-1]==' ':
            d=34
        elif isWay(dt[y][x-1]) and dt[y-1][x-1]==' ':
            d=41
        elif d==1 and dt[y-1][x]=='K' and dt[y][x+1]=='K':
            d=0
            wx,wy=(x,y-1)
        elif d==2 and dt[y][x+1]=='K' and dt[y+1][x]=='K':
            d=0
            wx,wy=(x+1,y)
        elif d==3 and dt[y+1][x]=='K' and dt[y][x-1]=='K':
            d=0
            wx,wy=(x,y+1)
        elif d==4 and dt[y][x-1]=='K' and dt[y+1][x]=='K':
            d=0
            wx,wy=(x-1,y)
        elif d==1 and isWay(dt[y-1][x]) and dt[y][x+1]=='K':
            d=1
            wx,wy=(x,y-1)
        elif d==2 and isWay(dt[y][x+1]) and dt[y+1][x]=='K':
            d=2
            wx,wy=(x,y+1)
        elif d==3 and isWay(dt[y+1][x]) and dt[y][x-1]=='K':
            d=3
            wx,wy=(x-1,y)
        elif d==4 and isWay(dt[y][x-1]) and dt[y-1][x]=='K':
            d=4
            wx,wy=(x,y-1)
    return (wx,wy,d)


dispmaze(dt)
x,y=getStart(dt)
wx,wy = (0,0)
wx,wy,d=getNext(0,x,y,wx,wy)
print(x,y)
while dt[y][x] != 'G':
    if d==1:
        dt[y][x]='1'
        y-=1
    if d==2:
        dt[y][x]='2'
        x+=1
    if d==3:
        dt[y][x]='3'
        y+=1
    if d==4:
        dt[y][x]='4'
        x-=1
    if d==12:
        dt[y][x]='1'
        y-=1
        dt[y][x]='2'
        x+=1
    if d==23:
        dt[y][x]='2'
        x+=1
        dt[y][x]='3'
        y+=1
        d=3
    if d==34:
        dt[y][x]='3'
        y+=1
        dt[y][x]='4'
        x-=1
        d=4
    if d==41:
        dt[y][x]='4'
        x-=1
        dt[y][x]='1'
        y-=1
        d=1
    if d==0:
        if (wx,wy)==(x,y-1):
            d=4
            dt[y][x]='4'
        if (wx,wy)==(x+1,y):
            d=1
            dt[y][x]='1'
        if (wx,wy)==(x,y+1):
            d=2
            dt[y][x]='2'
        if (wx,wy)==(x-1,y):
            d=3
            dt[y][x]='3'
    wx,wy,d=getNext(d,x,y,wx,wy)
    print(wx,wy,d)
    dispmaze(dt)
    tm.sleep(2)

print("----- Goal -----")
