def LinearSearch(arr,x,found):
    for i in range (len(arr)):
        if arr[i] == x :
            return i
    return -1

arr = [100, 178, 500, 250]
cari = int(input("bilangan yang dicari: "))
found = 0
found = LinearSearch(arr,cari,found) 
if found!=-1:
    print("data ditemukan di index: ", found)
else:
    print("data tidak ditemukan")   