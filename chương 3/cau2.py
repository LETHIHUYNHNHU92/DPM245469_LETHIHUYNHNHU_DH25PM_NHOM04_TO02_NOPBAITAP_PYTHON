month = int(input("Nhap vao so thang:"))
if month in (1,3,5,7,8,10,12):
    print("Thang co 31 ngay")
elif month in (3,4,6,9,11):
    print("Thang co 30 ngay")
elif month == 2:
    year = int(input("Nhap vao mot nam bat ky: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
         print("Thang 2 co 29 ngay")
    else:
        print("Thang 2 co 28 ngay")


