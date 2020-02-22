
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


##with O(n) complexity:
numbers = list(map(int,input("Enter List: ").split(",")))
k = int(input("Enter value: "))
i = 0
list_temp = numbers.copy()
match = False
for e in numbers:
    list_temp.pop(i)
    if k - e in list_temp:
        match = True
        print(str(e) + " " + str(k-e))
    i += 1
    list_temp = numbers.copy()
print(match)


#print(any(map(lambda x: (k - x) in numbers, numbers)))

