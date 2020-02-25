#numbers=[3,4,-1,1]
#numbers=[1,2,0]
numbers = list(map(int,input("Enter List: ").split(",")))
numbers.sort()
print(numbers)
i=1
number_found=False
while(number_found==False):
    if i not in numbers:
        print(i)
        number_found=True
    i+=1
