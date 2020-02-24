
##with O(n^2) complexity:
##numbers=[1,2,3,4,5]
##newnumbers=[]
##i=0
##while(i<len(numbers)):
##    mult=1
##    j=0
##    while(j<len(numbers)): #for j in numbers:
##        mult*=numbers[j]   #mult*=j
##        j+=1
##    mult=int(mult/numbers[i])
##    newnumbers.append(mult)
##    i+=1
##print(newnumbers)      


##with O(n) complexity, in one pass and without using division:
from functools import reduce
numbers = list(map(int,input("Enter List: ").split(",")))
newnumbers=[]
i = 0
for number in numbers:
    list_temp = numbers.copy()
    list_temp.pop(i)
    result = reduce((lambda x, y: x * y), list_temp)
    newnumbers.append(result)
    i += 1
print(newnumbers)
