def progression(a,b,c):
    if a != "0" and b != "0" and c != "0":
        tempList = [a,b,c]
        b1 = int(tempList[1])-int(tempList[0])
        b2 = int(tempList[2])-int(tempList[1])
        r1 = int(tempList[1])/int(tempList[0])
        r2 = int(tempList[2])/int(tempList[1])

        if b2 == b1 :
            print("AP",int(c)+b1)
        elif r2 == r1:
            print("GP",int(c)*r1)
        else : 
            print("Unknown Series")
    elif a == "0" and b == "0" and c == "0":
        exit()

a,b,c = input().split(" ")
progression(a,b,c)