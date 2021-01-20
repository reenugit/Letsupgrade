first,last = [int(x) for x in input("Enter the range").split()]
print("Prime numbers between ",first," and ",last," is: ")
for each in range(first,last+1):
    count = 0
    if each == 1:
        print(each)
    else:
        for i in range(1,each+1):
            if each%i==0:
                count = count + 1
    if count in range(1,3):
        print(each)
    

        