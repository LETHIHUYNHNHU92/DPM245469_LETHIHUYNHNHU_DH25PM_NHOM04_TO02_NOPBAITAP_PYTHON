#Nhập vào một năm bất kỳ, kiểm tra năm đó có phải năm nhuần hay không. Biết 
#rằng: Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia 
#hết cho 400

year = int(input("Nhap vao mot nam bat ky: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} la nam nhuan.")
else:
    print(f"{year} khong phai la nam nhuan.")
    