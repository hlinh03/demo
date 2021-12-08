mon=["Toán", "Văn", "Anh", "Lý", "Hóa", "Sinh", "Sử", "Địa"]
diem=[]
for i in range (8):
    diem.append(float(input(str(mon[i]) + ": ")))
print("===============")
#Diem tung khoi
def diemtheokhoi(khoi):
    khoi=khoi[0]*2+khoi[1]+khoi[2]
    return khoi

A=[diem[mon.index("Toán")],diem[mon.index("Lý")],diem[mon.index("Hóa")]]
B=[diem[mon.index("Hóa")],diem[mon.index("Toán")],diem[mon.index("Sinh")]]
C=[diem[mon.index("Văn")],diem[mon.index("Sử")],diem[mon.index("Địa")]]
D=[diem[mon.index("Anh")],diem[mon.index("Toán")],diem[mon.index("Văn")]]

a=diemtheokhoi(A)
b=diemtheokhoi(B)
c=diemtheokhoi(C)
d=diemtheokhoi(D)

tohop=[['A',a],['B',b],['C',c],['D',d]]

for i in tohop:
    print ("Khối",i[0],":",i[1])

max=0; m=-1
for i in tohop:
    if i[1]>max:
        max=i[1]
        m=m+1
    else:
        m=m+1
khoinenchon=tohop[m]

print ('> Bạn nên chọn khối',khoinenchon[0])