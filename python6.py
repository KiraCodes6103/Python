import math

int1 = int (input("Enter the lower bound (included) "))
int2 = int(input("Enter the upper bound (excluded) "))
for i in range(int1,int2):
     flag = 0
     for j in range(2,int(math.sqrt(i))+1):
         
         if i%j==0:
             flag = 1
             break
         else :
             continue
     if flag == 1:
         continue
     else:
         if i==1:
             continue
         else :
             print(i)


