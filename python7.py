max=0

print ("Enter the numbers space seperated(maximum number being 9999) ==> ")
list1 = [int(i) for i in input().split()]
list2=[0]*10000
for i in range (len(list1)):
    list2[list1[i]]+=1
for i in range (0,10000):
    if list2[i]>=list2[max]:
        max=i
print ("Highest freqency element is ==> ", max)