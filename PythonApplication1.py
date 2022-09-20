FILE_IN="ExSort.IN"
FILE_OUT="ExSortXX.OUT"
double_per_file=4;

#Dem so file
file_counter=1

with open(FILE_IN) as file:
    #Mo cac file mini de viet du lieu
    f=open(FILE_OUT.replace("XX",str(file_counter)),"w")
    
    #Dem so thuc trong mang
    num_counter=0 

    #Mang chua cac gia tri cua du lieu lay tu trong file input 
    arr=[]
    for line in file:


        #Mang da day, sap xep mang va viet du lieu vao cac file mini
        if num_counter>=double_per_file:

            arr.sort()
            file_counter+=1
            for i in arr:
                f.write(str(i)+"\n")
            #Reset mang
            arr=[]
            num_counter=0

            #Mo tiep file mini khac de lam viec
            f=open(FILE_OUT.replace("XX",str(file_counter)),"w")
            
        arr.append(float(line))
        num_counter+=1

        #Neu trong mang van con du lieu thi viet vao trong 1 file tiep theo
    if arr:
        for i in arr:
            f.write(str(i)+"\n")
    f.close()
    
