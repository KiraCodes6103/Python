def func(list1, str):
    new_list = list1.split()
    for i in range (len(new_list)):
        new_list[i] = (int)(new_list[i])
    if str == "asc":
        new_list.sort()
        print (new_list)
    elif str== "desc":
        new_list.sort(reverse=True)
        print (new_list)
    elif str == "none":
        print(new_list)




list_def = input("Enter the numbers in space seperated form ==> ")
print("\n")
str = input("Enter the desired string (asc, desc or none) ==> ")


func(list_def, str)



