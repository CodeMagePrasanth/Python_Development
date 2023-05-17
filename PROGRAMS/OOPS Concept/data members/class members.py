class xy3:
    a = 20
    b = 30
ob1 = xy3()
ob2 = xy3()
xy3.a = 100
ob2.b = 200
print(ob1.a,ob1.b,sep =',')
print(ob2.a,ob2.b,sep =',')
print(xy3.a,xy3.b,sep =',')