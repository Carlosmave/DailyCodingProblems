numbers=[10,15,3,7]
k=17
i=0

while(i<len(numbers)): #for i in range(len(numbers)):
    j=0
    while(j<len(numbers)): #for j in range(len(numbers)):
        if(j!=i and numbers[i]+numbers[j]==k):
            print(str(numbers[i]) + " " + str(numbers[j]))
            print("true")
            break
        j+=1
    i+=1

##for x in numbers:
##    if any(x>10):
##        print(x)

#if any(x > 10 for x in numbers):
#    print("true")

#for i in range(len(numbers)):
#    print(i)
#    print("-")


##def findsome(arr,k):
##    if  len(arr)<2:
##        return False;
##for e in arr:
##    if k>e and (k-e) in arr:
##        return True
##return False


##L = list(map(int,input("Enter List: ").split()))
##k = int(input("Enter value: "))
##
##for i in L:
##    if (k - i) in L:
##        print("True",k-i,i)



def if_sum_is_k(list, k):
    i = 0
    list_temp = list.copy()
    match = False
    for e in list:
        list_temp.pop(i)
        if k - e in list_temp:
            match = True
        i += 1
        list_temp = list.copy()
    return match
