#split() ->tach chuoi thanh tung tu,trong ngoac la ki tu gi thi no lay ki tu do lam ranh gioi tach
#neu trong ngoac khong co gi thi lay khoang trang lam ranh gioi
# S = "Huynh Nhu".split() -> "Huynh""Nhu"
# S = "Huynh ,Nhu".split(,) -> "Huynh","Nhu"

#join(str)
#kitunoi.join(chuoi can noi)
#str=['Cam','Quyt']
#vi du '+'.join(str) => 'Cam+Quyt'

# strip() xoa khoang trong o dau va cuoi

#Cách xử lý khoảng trắng ở giữa
# Dùng replace() (Nếu chỉ có 1 loại ký tự):Thay thế một ký tự thành ký tự khác.
# Ví dụ: s.replace(' ', '') => Loại bỏ tất cả khoảng trắng, bao gồm cả khoảng trắng ở giữa.

# Dùng split() và join() :Đây là cách tốt nhất để đảm bảo chỉ còn đúng một khoảng trắng giữa các từ.
# Ví dụ: s = "A   B".split() => ['A', 'B']
# Sau đó: ' '.join(['A', 'B']) => 'A B'

# len(str) => tra ve do dai cua chuoi'
#vi du str = "ABCD" => 4

#lower() => chuyen ve chu thuong
#vi du str ="HUYNH NHU" str.lower()=>huynh nhu

#upper() chuyen ve chu hoa
# vi du str ="huynh nhu" str.lower()=> HUYNH NHU

#isalpha() kiem tra xem chuoi co phai chi chua chu cai hay khong
#vi du str="Huynh Nhu" str.isalpha() => true

#isdigit() kiem tra xem chuoi co phai chi chua chu so hay khong
#vi du str="Huynh Nhu" str.isalpha() => false

#isupper() kiem tra chu hoa(chi kiem  tra chu cai,trong chuoi co chu so van duoc)
#vi du 'H'.isupper() ->true
#vi du 'HUYNH 1244'.issupper() => true

#islower() kiem tra chu thuong(chi kiem  tra chu cai,trong chuoi co chu so van duoc)
#vi du 'H'.islower() ->false
#vi du 'huynhnhu 1244'.issupper() => true

#capitalize() chu cai dau cua tu viet hoa,con lai viet thuong
#vi du 'HUYNH'.capitalize()-> Huynh

#append them 1 phan tu vao chuoi
#str="1,2,4"
#str.append(11) =>str="1,2,4,11"

# rsplit(ranh gioi dung tach,so lan tach)
# str ="Huynh//Nhu"     str.rsplit(//,1)[-1] => 'Nhu ' ( bo luon //)
#[-1] duoc dinh nghia la phan tu cuoi cung cua list
#[-2] la phan tu ap chot

#count() dem so lan xuat hien cua phan tu trong list
#vi du:list=[1,2,4,5,6,7,]
#list.count(4) => dem so lan xuat hien cua 5 trong list

#ham sap xep sort
#list=[2,6,3,8,2,32,]
#list.sort() => sap xep tang dan(mac dinh)
#list.sort(reverse = true) => sap xep giam dan 
# sort() :sap xep truc tiep tren list goc
# sorted():sap xep tren list moi,list goc con nguyen
#Vi du:lst_moi = sorted(lst)

#remove xoa ki tu xuat hien dau tien trong list
#vi du:list=[1,2,4,5,6,7,]
#list.remove(4) =>list=[1,2,5,6,7]



