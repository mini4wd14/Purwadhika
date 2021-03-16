def nohp(a):
    listNo = []
    finalNo = ""
    for i in a:
        listNo.append(i)
    if listNo[0] != '0' and listNo[1] != '8':
        print("Nomor HP harus dimulai dengan","08")
    elif len(listNo) > 13:
        print("Nomor HP hanya maksimal 13 angka")
    elif listNo[0] == '0' and listNo[1] == '8' and len(listNo) < 13:
        for i in listNo:
            finalNo += i
        print("Nomor HP saya adalah",finalNo)

a = input("Masukan nomor HP : ")
nohp(a)


