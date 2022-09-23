import os
#os dung de check file con du lieu k
FILE_IN = "ExSort.IN"
FILE_OUT = "ExSortXX.OUT"

# TODO: Doi sang so luong phan tu float trong file
double_per_file = 62499840

# Dem so file
file_counter = 1

with open(FILE_IN) as file:
    # Mo cac file mini de viet du lieu
    f = open(FILE_OUT.replace("XX", str(file_counter)), "wb")

    # Dem so thuc trong mang
    num_counter = 0

    # Mang chua cac gia tri cua du lieu lay tu trong file input
    arr = []
    for line in file:

        # Mang da day, sap xep mang va viet du lieu vao cac file mini
        if num_counter >= double_per_file :

            arr.sort()
            file_counter += 1
            for i in arr:
                s = str(i) + "\n"
                bt = s.encode()
                f.write(bt)
            # Reset mang
            arr = []
            num_counter = 0

            # Mo tiep file mini khac de lam viec
            f = open(FILE_OUT.replace("XX", str(file_counter)), "wb")

        arr.append(float(line))
        num_counter += 1

        # Neu trong mang van con du lieu thi viet vao trong 1 file tiep theo
    if arr:
        arr.sort()
        for i in arr:
            s = str(i) + "\n"
            bt = s.encode()
            f.write(bt)
    f.close()

def getFirstElementOfFile(i):
    with open(FILE_OUT.replace("XX", str(i)), 'rb') as f:
        for line in f:
            return float(line)

def deleteFirstElementOfFile(i):
    M = []
    with open(FILE_OUT.replace("XX", str(i)), 'rb') as file_running:
        for ln in file_running:
            x = float(ln)
            M.append(x)
        # Xoa dmin ra khoi segmet chua no
        M.pop(0)
        f_write = open(FILE_OUT.replace("XX", str(i)), 'wb')
        for i in M:
            a = str(i) + "\n"
            a = a.encode()
            f_write.write(a)
        f_write.close()

floatToFileNumber=dict()

L=[] #L la array buffer

for i in range(1, file_counter + 1):
     t=getFirstElementOfFile(i)
     deleteFirstElementOfFile(i)
     #Map gia tri vua them vao voi 1 
     floatToFileNumber[t]=i
     L.append(t)
     L.sort()
        
fileout = open("ExSort.OUT",'wb')
while L: #is not empty
     s = str(L[0]) + "\n"
     s=s.encode()
     fileout.write(s)

     #Kiem tra neu file cua phan tu vua pop ra con du lieu khong
     #Neu file con phan tu thi lay phan tu tiep theo cua file
     #Neu file het phan tu thi khong xu ly ma qua vong lap while tiep theo
     f=FILE_OUT.replace("XX", str(floatToFileNumber[L[0]]))
     if os.stat(f).st_size>0:
         i=getFirstElementOfFile(floatToFileNumber[L[0]])
         deleteFirstElementOfFile(floatToFileNumber[L[0]])

         #Kiem tra neu i co lap lai khong, neu lap lai thi lay phan tu ke tiep
         while os.stat(f).st_size>0 and i==L[0]:
             i=getFirstElementOfFile(floatToFileNumber[L[0]])
             deleteFirstElementOfFile(floatToFileNumber[L[0]])

         #Kiem tra edge case, neu cac phan tu con lai cua file deu la phan tu trung lap voi L[0]
         #thi i van luu gia tri trung lap mac du file da het
         if i!=L[0]:
             L.append(i)
             floatToFileNumber[i]=floatToFileNumber[L[0]]
             L.sort()
         #Xoa key cu ra khoi map
         floatToFileNumber.pop(L[0])
     L.pop(0)
     
            
fileout.close()
