import numpy as np
import math
C=24

"""x1=1.9
x2=3.1
x3=4"""

x1=1.8
x2=3.2
x3=4.2

er=4

print("x1: ",x1,"\t\tx2:",x2,"\t\tx3:",x3)
fx=np.matrix([[round(pow(x1,2)+(x2*x3)-16,er)],[round((x1*x2)+x3-10,er)],[round(x1+pow(x2,2)+(C*x3)-15,er)]])
fpx=np.matrix([[round((2*x1),er),round(x3,er),round(x2,er)],[round(x2,er),round(x1,er),round(1,er)],[round(1,er),round((2*x2),er),round(C,er)]])

print("fx")
print(fx)
print("fpx")
print(fpx)

deltx=fpx**(-1)*-fx
print("deltx")
print(deltx)

print("Segunda Iteración")

x1=round(x1+round(deltx.item(0,0),er),er)
x2=round(x2+round(deltx.item(1,0),er),er)
x3=round(x3+round(deltx.item(2,0),er),er)

print("x1: ",x1,"\t\tx2:",x2,"\t\tx3:",x3)

fx=np.matrix([[round(pow(x1,2)+(x2*x3)-16,er)],[round((x1*x2)+x3-10,er)],[round(x1+pow(x2,2)+(C*x3)-15,er)]])
fpx=np.matrix([[round((2*x1),er),round(x3,er),round(x2,er)],[round(x2,er),round(x1,er),round(1,er)],[round(1,er),round((2*x2),er),round(C,er)]])

print("fx")
print(fx)
print("fpx")
print(fpx)

deltx=fpx**(-1)*-fx
print("deltx")
print(deltx)

print("Tercera Iteración")


x1=round(x1+round(deltx.item(0,0),er),er)
x2=round(x2+round(deltx.item(1,0),er),er)
x3=round(x3+round(deltx.item(2,0),er),er)

print("x1: ",x1,"\t\tx2:",x2,"\t\tx3:",x3)


print("------------------------------------------------------")
xx1=1
xx2=3
ex=2

print("xx1: ",xx1,"\t\txx2:",xx2)
ffx=np.matrix([[round(pow(xx1,2)-xx2+1.69,ex)], [round(20*xx1*math.sin(xx1)-xx2-16.7,ex)]])
ffpx=np.matrix([[round(2*xx1,ex),-1],[round(((20)*math.sin(xx1))+((20*xx1)*math.cos(xx1)),ex),-1]])

print("ffx")
print(ffx)
print("ffpx")
print(ffpx)
#print(np.dot(aux1,aux2))
delx = ffpx**(-1)*-ffx

print("delx")
delx[0][0]=round(delx.item(0,0),4)
delx[1][0]=round(delx.item(1,0),3)
print(delx)

print("Segunda Iteración")
xx1=xx1+delx.item(0,0)
xx2=xx2+delx.item(1,0)
print("xx1: ",xx1,"\t\txx2:",xx2)
ex=8
ffx2=np.matrix([[round(pow(xx1,2)-xx2+1.69,ex)], [round(20*xx1*math.sin(xx1)-xx2-16.7,ex)]])
ffpx2=np.matrix([[round(2*xx1,ex),-1],[round(((20)*math.sin(xx1))+((20*xx1)*math.cos(xx1)),ex),-1]])

print("ffx 2")
print(ffx2)
print("ffpx 2")
print(ffpx2)

delx2 = ffpx2**(-1)*-ffx2
print("delx 2")
delx2[0][0]=round(delx2.item(0,0),7)
delx2[1][0]=round(delx2.item(1,0),7)
print(delx2)

print("Tercera Iteración")
xxx1=round(xx1+delx2.item(0,0),7)
xxx2=round(xx2+delx2.item(1,0),7)
print("xxx1: ",xxx1,"\t\txxx2:",xxx2)
