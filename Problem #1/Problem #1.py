
##with O(n^2) complexity:
##numbers=[10,15,3,7]
##k=17
##i=0
##
##while(i<len(numbers)):
##    j=0
##    while(j<len(numbers)): #for j in range(len(numbers)):
##        if(j!=i and numbers[i]+numbers[j]==k):
##            print(str(numbers[i]) + " " + str(numbers[j]))
##            print("true")
##            break
##        j+=1
##    i+=1


##with O(n) complexity and in one pass:
numbers = list(map(int,input("Enter List: ").split(",")))
k = int(input("Enter value: "))
i = 0
match = False
for number in numbers:
    list_temp = numbers.copy()
    list_temp.pop(i)
    if k - number in list_temp:
        match = True
        print(str(number) + " " + str(k-number))
    i += 1
print(match)


#print(any(map(lambda x: (k - x) in numbers, numbers)))
##print(list(map(lambda x: (k - x) in numbers, numbers)))

