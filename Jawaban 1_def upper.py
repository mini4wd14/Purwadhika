def upper(a):
    tempList =[]
    finalList = ["*","*"]
    finalWords = ""
    if len(a) > 200 :
        print("Batas karakter maksimal hanya 200")
    elif a == "":
        print("Masukkan sebuah inputan")
    else:
        tempList=list(a.split(" "))

        for i in tempList:
            finalList.insert(-1,i)

        convertList = [x.upper() for x in finalList]
        for i in convertList:
            finalWords += i
        print(finalWords)

a = input("Masukan sebuah kalimat : ")
upper(a)
