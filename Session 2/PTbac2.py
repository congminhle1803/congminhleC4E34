print ("Cho phuong trinh bac 2: ax^2 + bx + c = 0")

a = int(input("Nhap gia tri a = "))
b = int(input("Nhap gia tri b = "))
c = int(input("Nhap gia tri c = "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0: # = la phep gan, == dung de the hien dieu kien, phep so sanh
    x = -b/(2*a)
    print("Phuong trinh co nghiem kep: {0}".format(x))
else:
    x1 = (-b-delta**0.5)/(2*a)
    x2 = (-b+delta**0.5)/(2*a)
    print("Phuong trinh co 2 nghiem phan biet: {0} va {1}".format(x1, x2))
   
#format tra lai ket qua theo thu tu sap xep. Trong vi du trong bai la 0 va 1