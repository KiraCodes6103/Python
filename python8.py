from re import I

sum = 0
str1 = input("Enter the desird string ==> ")
temp=""
for i in str1 :
    if(i.isdigit()):
        temp+=i
list = []
for i in range(len(temp)):
    list.append(int(temp[i:i+1]))
for i in range(len(list)):
    sum+=list[i]
print (sum)