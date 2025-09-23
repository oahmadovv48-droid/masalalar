# 1- dars.Kiritish,chiqarish va o'zlashtirish operatoriga oid masalalar.
# 1- misol.
"""a=int(input("a ni kiriting"))
P=4*a
print(P)"""

# 2- misol.
"""a=int(input("a ni kiriting="))
S=a**2
print(S)"""

# 3 - misol.
"""a=int(input("a ni kiriting="))
b=int(input("b ni kiriting="))
S=a*b
P=2*(a+b)
print(S,P)"""

# 4 - misol.
"""pi = 3.14
d=int(input("Aylananing diametrini kiriting="))
L=pi*d
print(L)"""

# 5 - misol.
"""a=int(input('Kubning yon tomonini kiriting a='))
V=a**3
S=6*(a**2)
print(V,S)"""

# 6 - misol.
"""a=int(input("a ni kiriting="))
b=int(input("b ni kiriting="))
c=int(input("c ni kiriting="))
V=a*b*c
S=2*(a*b+b*c+a*c)
print(V,S)"""

# 7- misol.
"""R=int(input("doiraning radiusini kiriting="))
pi=3.14
L=2*pi*R
S=pi*R**2
print("Doiraning uzunligi",  L ,"ga teng")
print("Doiraning yuzasi", S,"ga teng")"""

# 8- misol.
"""a=int(input("a ni kiriting"))
b=int(input("b ni kiriting"))
S=(a+b)/2
print(S)"""

# 9- misol.
"""import math
a=int(input("a ni kiriting="))
b=int(input("b ni kiriting="))
G= math.sqrt(a+b)
print(G)"""

# 10- misol.
"""a=int(input("0<a a ni kiriting="))
b=int(input("0<b b ni kiriting="))
s=a+b
k=a*b
sq1=a**2
sq2=b**2
print("yig'indisi=",s,"ko'paytmasi=",k)
print("a ning kvadrati",sq1,",b ning kvadrati",sq2)"""

# 11- misol.
"""a=int(input("a="))
b=int(input("b="))
Y=a+b
print("Sonlar yig'indisi",Y,"ga teng")
S=a*b
print("Sonlar ko'paytmasi",S,"ga teng")
mod1=abs(a)
mod2=abs(b)
print("a ning moduli",mod1,"b ning moduli",mod2)"""

# 12- misol.
"""import math
a=int(input("a katetni kiriting="))
b=int(input("b katetni kiriting="))
c= math.sqrt(a**2+b**2)
P=a+b+c
print("Gipotenuza=",c,"Peremetri=",P)"""

# 13- misol.
"""import math
R1=int(input("R1="))
R2=int(input("R2="))
S1=math.pi*R1
S2=math.pi*R2
S3=math.pi*(R1-R2)
print("Aylanalarning yuzalari",S1,S2)
print("Yuzalar ayirmasi",S3)"""

# 14- misol.
"""import math
L=int(input("Aylana uzunligini kiriting L="))
r=L/(2*math.pi)
S=math.pi*r**2
print("Aylana radiusi",r,"Yuzasi",S,"ga teng")"""

# 15- misol.
"""import math
S=int(input("Aylananing yuzasini kiriting="))
r=math.sqrt(S/math.pi)
d=2*r
print("Aylana radiusi",r)
print("Aylana diametri",d)"""

# 16- misol.
"""x1=int(input("x1 nuqtani kiriting"))
x2=int(input("x2 nuqtani kiriting"))
print("Nuqtalar orasidagi masofa=",x2-x1)"""

# 17- misol.
"""A=int(input("A nuqtani kiriting"))
B=int(input("B nuqtani kiriting"))
C=int(input("C nuqtani kiriting"))
AB=A+B
AC=A+C
BC=B+C
S=AB+AC+BC
print("AC kesma uzunligi=",AC,"BC kesma uzunligi=",BC,"ga teng")
print("Kesmalar yig'indisi",S,"ga teng")"""

# 18- misol.
"""A=int(input("A nuqtani kiriting"))
B=int(input("B nuqtani kiriting"))
C=int(input("C nuqtani kiriting"))
AC=abs(C-A)
BC=abs(B-C)
print("AC*BC=",AC*BC)"""

# 19- misol.
"""x1=int(input("x1="))
x2=int(input("x2="))
y1=int(input("y1="))
y2=int(input("y2="))
a=abs(x2-x1)
b=abs(y2-y1)
P=2*(a+b)
S=a*b
print("To'rtburchak peremetri=",P)
print("To'rtburchak yuzasi=",S)"""

# 20- misol.
"""import math
x1=int(input("x1="))
x2=int(input("x2="))
y1=int(input("y1="))
y2=int(input("y2="))
S=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Masofa=",S)"""

# 21- misol.
"""import math
x1=int(input("x1="))
x2=int(input("x2="))
x3=int(input("x3="))
y1=int(input("y1="))
y2=int(input("y2="))
y3=int(input("y3="))
a=math.sqrt((x2-x1)**2+(y2-y1)**2)
b=math.sqrt((x3-x2)**2+(y3-y2)**2)
c=math.sqrt((x1-x3)**2+(y1-y3)**2)
P=a+b+c
print("Uchburchak peremetri=",P)
P=P/2
S=math.sqrt(P*(P-a)*(P-b)*(P-c))
print("Uchburchak yuzasi",S)"""

# 22- misol.
"""A=int(input("A="))
B=int(input("B="))
A, B=B, A
print("A=",A)
print("B=",B)"""

# 23- misol.
"""A=int(input("A="))
B=int(input("B="))
C=int(input("C="))
A, B=B, A
B, C=C, B
C, A=A, C
print("A=",A,"B=",B,"C=",C)"""

# 24- misol.
"""A=int(input("A="))
B=int(input("B="))
C=int(input("C="))
A, C=C, A
C, B=B, C
B, A=A, B
print("A=",A,"B=",B,"C=",C)"""

# 25- misol.
"""x=float(input("x ga qiymat kiriting="))
y=3*x**6-6*x**2-7
print("Y=",y)"""

# 26- misol.
"""x=float(input("x ga qiymat kiriting="))
y=4*((x-3)**6)-7*((x-3)**3)+2
print("Y=",y)"""

# 27-28 misol.
"""A=int(input("A="))
a=int(input("a="))
S=A**a
print(S)"""

# 29- misol.
"""import math
a=float(input("Burchakni kiriting (0<a<360)="))
r = a*math.pi / 180
print("Radian=",r)"""

# 30- misol.
"""import math
a=float(input("a burchakni kiriting (0<a<2pi)="))
C=a*180/math.pi
print("Gradus C=",C)"""

# 31- misol.
"""Tf=float(input("Tempraturani farangeytda kiriting="))
TC=(Tf-32)*5/9
print("Tempratura selsiy=",TC)"""

# 32-misol.
"""C=float(input("Tempraturani selsiyda kiriting="))
F=(C*9/5)+32
print("Tempratura farangeyt=",F)"""

# 33- misol.
"""X=float(input("Konfet kg ni kiriting->"))
A=float(input("Konfetni narxini kiriting->"))
Y=float(input("Qancha kg konfet->"))
sum=A/X
sum2=Y*sum
print("Bir kg konfet narxi:",sum,"so'm")
print(Y,"kg konfet narxi",sum2,"so'm")"""

# 34- misol.
"""X=float(input("Shokalad kg ni kiriting->"))
A=float(input("Shokaladni narxini kiriting:"))
Y=float(input("Konfet kg ni kiriting->"))
B=float(input("Konfetni narxini kiriting->"))
shokalad=A/X
konfet=B/Y
narx=shokalad-konfet
print("Shokalad konfetdan",narx, "so'm qimmat")"""

# 35- misol.
"""V=float(input("Qayiqning tezligini kiriting:"))
U=float(input("Daryo oqimi tezlidini kiriting:"))
t1=float(input("Oqim bo'yicha xarakatlanish vaqti:"))
t2=float(input("Oqimga qarshi xarakatlanish vaqti:"))
Vob=V+U        #Oqim bo'yicha xarakatlanish tezligini aniqlash
Voq=V-U        #Oqimga qarshi harakatlanish tezligini aniqlash
S1=Vob*t1
S2=Voq*t2
S=S1+S2
print("Qayiqni yurgan yo'li:",S,"ga teng")"""

# 36-misol.
"""V1=float(input("Birinchi avtomobil tezligi:"))
V2=float(input("Ikkinchi avtomobil tezligi:"))
S=float(input("Avtomobillar orasidagi masofani kiriting:"))
T=float(input("T vaqtni kiriting:"))
U=V1+V2
St=S+U*T
print("T vaqtdan keyin ular orasidagi masofa:",St,"ga teng")"""

# 37-misol.
"""V1=float(input("Birinchi avtomobil tezligi:"))
V2=float(input("Ikkinchi avtomobil tezligi:"))
S=float(input("Avtomobillar orasidagi masofani kiriting:"))
T=float(input("T vaqtni kiriting:"))
U=V1+V2
St=S-U*T
print("T vaqtdan keyin ular orasidagi masofa:",St,"ga teng")"""

# 38- misol.
"""A=float(input("A="))
B=float(input("B="))
x=-B/A
print("X ning qiymati:",x)"""

# 39-misol.
"""import math
A=float(input("A="))
B=float(input("B="))
C=float(input("C="))
D=B**2-4*A*C
X1=(-B-math.sqrt(D))/(2*A)
X2=(-B+math.sqrt(D))/(2*A)
print("X1=",X1,"X2=",X2)"""

# 40- misol.
"""A1=float(input("A1="))
B1=float(input("B1="))
C1=float(input("C1="))
A2=float(input("A2="))
B2=float(input("B2="))
C2=float(input("C2="))
D=A1*B2-A2*B1
x=(C1*B2-C2*B1)/D
y=(A1*C2-A2*C1)/D
print("X=",x,"Y=",y)"""






















