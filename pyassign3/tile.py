"""tile.py: 对一面m*n的墙用x*y的砖进行密铺，
            打印出所有/部分密铺方案，
            并在turtle模块上实现可视化。
__author__ = "Yi Congwei"
__pkuid__  = "1800011850"
__email__  = "yicw@pku.edu.cn"
"""

import turtle
    
def built_wall(m,n):
    '''
    造m*n的空墙
    '''
    list=[]
    for i in range(m*n):
        list.append(i)
    return list


def brick(x,y,a,b,m,n,wall):
    '''
    将以(x,y)为左下顶点的a*b的砖块打包,并确定填充状态。
    '''
    bricklist=[]
    for i in range(x,x+a):
        for j in range(y,y+b):
            f=i+j*m
            bricklist.append(f)
            wall[f]=0# 将位置f的已填充状态标记为零              
    bricktuple=tuple(bricklist)# 砖块list元组化
    return bricktuple

def anti_brick(x,y,a,b,m,n,wall):
    '''
    陷入递归而对list的改变不可逆deeocopy又学不会而写的函数。
    用于拆墙，即将变成0的位点复原为f（可铺状态）。

    '''
    for i in range(x,x+a):
        for j in range(y,y+b):
            f=i+j*m
            wall[f]=f
      
def judge(a,b,m,n,wall,f):
    '''
    判断f位置能否放入一个a*b的砖块。
    '''
    if f%m+a>m or f//m+b>n:# 判断以l为左下角的能放一个
        return False
    else:
        true=True
        for h in range(f,f+a):
            for v in range(h,h+m*b,m):
                if v not in wall:#判断以l为左下角的a*b大小里是否已填过砖
                    true=False
        return true
                    
    
def brick_paving(a,b,m,n,wall,f):
    '''
    在f位置可以放入a*b的情况下，开始添砖直到最后一格。
    '''
    methods=[]
    if f==m*n:# 铺到头啦，输出空
        return[[]]
    while f not in wall:# 如果这个位置已经被填了，不要递归找啦直接看下一个砖（之前被坑到memoryerror
        f+=1
        if f==m*n:
            return[[]]
    for (a,b) in [(a,b),(b,a)]:# 横铺与竖铺
        if judge(a,b,m,n,wall,f) is True:
            x=f%m#得到坐标
            y=f//m
            one_brick=brick(x,y,a,b,m,n,wall)#得到砖块
            some=brick_paving(a,b,m,n,wall,f+1)#往一个位点铺
            for one in some:#把砖块放进一个方法中去
                one.append(one_brick)
            methods.extend(some)#方法+1
            anti_brick(x,y,a,b,m,n,wall)#恢复未填砖的情况
    return methods

def tile(a,b,m,n,wall,f=0):
    '''
    由于a=b的情况也是当作a,b和b,a两种情况处理的所以正方形砖只有一种拼法，实际上函数当作了2**（m*n/a/b）种方法，故只保留一种。
    另外为了符合题目示例将铺法的表示为从0开始的函数了。
    '''
    methods=brick_paving(a,b,m,n,wall,f)
    l=len(methods)
    tiles= []
    if a==b:
        methods[0].reverse()
        tiles.append(methods[0])
    else:
        for i in range(l):
            methods[i].reverse()
            tiles.append(methods[i])
    return tiles
        
def visualization(method,a,b,m,n):
    s=a*b
    if m>=n:# 调整合适画布尽管很丑
        turtle.setworldcoordinates(-m/10,-m/10,m/10+m,m/10+m)
    else:
        turtle.setworldcoordinates(-n/10,-n/10,n/10+n,n/10+n)
    pen=turtle.Turtle()
    turtle.title('方案可视化')
    pen.speed(0)
    pen.ht()
    pen.color('pale turquoise')
    for i in range(n+1):# 打墙基
        pen.up()
        pen.goto(0,n-i)
        pen.down()
        pen.goto(m,n-i)
    for j in range(m+1):
        pen.up()
        pen.goto(m-j,n)
        pen.down()
        pen.goto(m-j,0)
    pen.color('indigo')
    pen.pensize(4)
    #开始将一维点阵二维化，以实现每块砖的填充。
    if a*b!=1:
        for tile in method:
            x1=tile[0]%m
            y1=tile[0]//m
            x2=tile[s-1]%m+1
            y2=tile[s-1]//m+1
            pen.up()
            pen.goto(x1,y1)
            pen.down()
            pen.goto(x1,y2)
            pen.goto(x2,y2)
            pen.goto(x2,y1)
            pen.goto(x1,y1)
            pen.up()
    else:
        for tile in method:
            x1=tile[0]%m
            y1=tile[0]//m
            x2=x1+1
            y2=y1+1
            pen.up()
            pen.goto(x1,y1)
            pen.down()
            pen.goto(x1,y2)
            pen.goto(x2,y2)
            pen.goto(x2,y1)
            pen.goto(x1,y1)
            pen.up()
    
    
def main():            
    m=int(input('墙长：'))
    n=int(input('墙高：'))
    a=int(input('砖长：'))
    b=int(input('砖宽：'))
    wall=built_wall(m,n)
    methods=tile(a,b,m,n,wall,f=0)
    number=len(methods)
    if number==0:
        print('不可能完全铺满哒')
    else:
        print('一共有'+str(len(tile(a,b,m,n,wall,f=0)))+'种铺法')
        if number<=20:
            for i in range(number):
                print('第'+str(i+1)+'种：',methods[i])
            t=int(turtle.numinput('方案可视化', '请输入你要可视化的方案号码', 1, 1, number))
            visualization(methods[t-1],a,b,m,n)
        else:
            print('由于数量太多我就不全部打出来了。')
            cy=input('请选择一部分方案（所选择的区间序号之间用空格打出）：').split()
            if int(cy[0])>number or int(cy[-1])>number:
                cy=input(('请重新输入区间序号，不要超过总方案数：：')).split()
            if int(cy[0])>int(cy[-1]):
                for i in range(int(cy[-1]),int(cy[0])+1):
                    print('第'+str(i)+'种：',methods[i])
                t=int(turtle.numinput('方案可视化', '请输入你要可视化的方案号码', int(cy[-1]),int(cy[-1]),int(cy[0])))
                visualization(methods[t-1],a,b,m,n)
            else:
                for i in range(int(cy[0]),int(cy[-1])+1):
                    print('第'+str(i)+'种：',methods[i])
                t=int(turtle.numinput('方案可视化', '请输入你要可视化的方案号码', int(cy[0]),int(cy[0]),int(cy[-1])))
                visualization(methods[t-1],a,b,m,n)
            
if __name__ == '__main__':
    main()
   
