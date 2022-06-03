from xml.dom.minidom import CharacterData
def converter(str):
    list_str = []
    list_str2 = []
    for i in range(len(str)):
        list_str.append(str[i:i+1])

    for i in range(len(list_str)):
        list_str2.append(2*list_str[i])
    str2 = ""
    for i in range(len(list_str2)):
        str2+= list_str2[i]
    return str2



str = input("Enter the string  ")
str2 = converter(str)
print(str2)