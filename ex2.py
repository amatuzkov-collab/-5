import turtle
xc=int(input())
yc=int(input())
r=int(input())
x=int(input())
y=int(input())
turtle.penup()
turtle.goto(xc,yc-r)
turtle.pendown()
turtle.circle(r)
turtle.penup()
turtle.goto(x,y)
turtle.dot(5)
turtle.penup()
turtle.goto(20,0)

if ((xc-x)**2+(yc-y)**2)**0.5<r:
    print('точка внутри окружности')
elif ((xc-x)**2+(yc-y)**2)**0.5==r:
    print('точка на окружности')
else:
    print('точка вне окружности')

