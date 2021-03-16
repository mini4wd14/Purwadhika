def pattern_tri(a):
    n = 1
    for i in range(a-2,0,-1):
        if i == a-2:
            print(" "*(i+1) + "***")
        print(" "*i + "**" + " "*n + "**")
        n += 2
        if i == 1:
            print("*"*2*a + "*")

a = int(input("Masukan jumlah baris : "))
pattern_tri(a)