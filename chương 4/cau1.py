from math import sqrt 

print("Chương trính tính diện tích tam giac:")
a = float(input("nhap canh thu nhat:"))
b = float(input("Nhap canh thu hai:"))
c = float(input("Nhap canh thu ba:"))

if (a<=0 or b <=0 or c <=0) or (a+b)<=c or (a+c)<=b or b+c<=a: 
    print("Tam giác không hợp lệ") 
else: 
    cv=a+b+c 
    p=cv/2 
    dt=sqrt(p*(p-a)*(p-b)*(p-c)) 
    print("Diện tích =",dt)