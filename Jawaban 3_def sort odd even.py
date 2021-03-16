def sort_odd_even(a):
    even = []
    odd = []
    for i in a:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    even.sort(reverse=True)
    odd.sort()
    finalList = odd + even
    print(finalList)

sort_odd_even([1,3,2,2,1,5,1,24,12,124,12,21,32,15])