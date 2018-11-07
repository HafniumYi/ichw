import turtle
import math
colors=['blue','yellow','green','red', 'sea green', 'brown']
turtle.setworldcoordinates(-520,-450,520,450)

b=turtle.Screen()
b.bgcolor('black') 

sun=turtle.Turtle()
sun.color('orange')
sun.shape('circle')
sun.shapesize(0.5,0.5,0.5)

def pl(p,n):
    p.shape('circle')
    p.speed(0)
    p.shapesize(0.3,0.3,0.3)
    p.color(colors[n%6])
    
m=turtle.Turtle()#Mercury
pl(m,1)
v=turtle.Turtle()#Venus
pl(v,2)
e=turtle.Turtle()#Earth
pl(e,3)
ms=turtle.Turtle()#Mars
pl(ms,4)
j=turtle.Turtle()#Jupiter
pl(j,5)
s=turtle.Turtle()#Saturn
pl(s,6)
t=[m,v,e,ms,j,s]
def plantes():
    for a in range(0,1076040):
        x0=[19.3*math.cos(20*a*math.pi/180)+4, 36*math.cos(20*a*math.pi/180/3), 50*math.cos(20*a*math.pi/180/4),
            75*math.cos(20*a*math.pi/180/7), 240*math.cos(20*a*math.pi/180/49), 440*math.cos(20*a*math.pi/180/122)]
        
        y0=[17*math.sin(20*a*math.pi/180), 36*math.sin(20*a*math.pi/180/3), 50*math.sin(20*a*math.pi/180/4),
            75*math.sin(20*a*math.pi/180/7), 240*math.sin(20*a*math.pi/180/49), 440*math.sin(20*a*math.pi/180/122)]
        
        x1=[19.3*math.cos(20*(a+1)*math.pi/180)+4, 36*math.cos(20*(a+1)*math.pi/180/3), 50*math.cos(20*(a+1)*math.pi/180/4),
            75*math.cos(20*(a+1)*math.pi/180/7), 240*math.cos(20*(a+1)*math.pi/180/49), 440*math.cos(20*(a+1)*math.pi/180/122)]
        
        y1=[17*math.sin(20*(a+1)*math.pi/180), 36*math.sin(20*(a+1)*math.pi/180/3), 50*math.sin(20*(a+1)*math.pi/180/4),
            75*math.sin(20*(a+1)*math.pi/180/7), 240*math.sin(20*(a+1)*math.pi/180/49), 440*math.sin(20*(a+1)*math.pi/180/122)]
    
        for i in range(6):
            t[i-1].up()
            t[i-1].goto(x0[i],y0[i])
            t[i-1].down()
            t[i-1].goto(x1[i],y1[i])
    plantes()
    
plantes()