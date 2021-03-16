def max_words(a):
    tempList = []
    checkList = []
    lenWords = 0
    tempList=a.split(" ")
    for i in tempList:
        if len(i) >= lenWords:
            lenWords = len(i)
    for i in tempList:
        if len(i) == lenWords:
            checkList.append(i)
            
    print("Jumlah karakter terbanyak adalah sebesar",lenWords,"karakter")
    for i in checkList:
        print("Karakter yang berjumlah",lenWords,"adalah",i)

a = input("Masukan sebuah kalimat : ")
max_words(a)

