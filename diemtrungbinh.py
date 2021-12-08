dsmon = ['TCC', 'GTN', 'TDLT', 'KTVM', 'TTHCM', 'LLNNPL']
dstinchi = [3, 2, 3, 3, 2, 3]
dssv = []; dsdiemcacmon = []; drl = []; dsdtb = []

def nhapdssv():
    dssv.append(input('Tên: '))

def nhapdrl():
    drl.append(float(int(input('+ Điểm rèn luyện: '))))

def nhapdiem():
    for i in range(len(dsmon)):
        dsdiemcacmon.append(int(input('- '+dsmon[i]+': ')))

def diemtb1sv(dsdiemcacmon, dstinchi, drl):
    tongdiem = 0
    for i in range(len(dsmon)):
        tongdiem += dsdiemcacmon[i]*dstinchi[i]
    for j in range(len(dssv)):
        dtb = round(tongdiem/sum(dstinchi)+drl[j]*0.2, 2)
    return dtb

#Nhập danh sách sinh viên và điểm
n = int(input('TỔNG SỐ SINH VIÊN: '))
print()
for i in range(n):
    nhapdssv()
    nhapdrl()
    nhapdiem()
    dsdtb.append(diemtb1sv(dsdiemcacmon, dstinchi, drl))
    print('==============================')

#Lấy danh sách các sinh viên lấy học bổng
m = int(input('SỐ SINH VIÊN NHẬN HỌC BỔNG: '))
print()
for k in range(m):
    a=dsdtb.index(max(dsdtb))
    dssv.pop(a)
    dsdtb.pop(a)
    print(dssv[a]+' - '+str(dsdtb[a]))