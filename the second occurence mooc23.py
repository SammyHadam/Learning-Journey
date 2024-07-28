string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

string1 = ' '
string2 = ' '
index = string.find(substring)


if substring in string:
    if len(substring) >= 2:
        string1 = string[index:index+len(substring)]
        string2 = string[index+len(substring):]
        index1 = string2.find(substring)
        if substring in string2:
            output = string2[index1:index1+len(substring)]
            print(f"The second occurrence of the substring is at index {index1+index+len(substring)}.")
        else:
            print("The substring does not occur twice in the string.")  
    elif len(substring) == 1:
        string1 = string[index:index+len(substring)]
        string2 = string[index+len(substring):]
        index1 = string2.find(substring)
        if substring in string2:
            output = string2[index1:index1+len(substring)]
            print(f"The second occurrence of the substring is at index {index1+index+1}.")  
        else:
            print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")