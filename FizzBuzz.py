def fizzbuzz(a):
    for i in range(1,a+1):
        if i % 3 != 0 and i % 5 != 0 :
            print(i)
        elif i % 3 == 0 and i % 5 == 0 :
            print("FizzBuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print ("Buzz")

fizzbuzz(20)