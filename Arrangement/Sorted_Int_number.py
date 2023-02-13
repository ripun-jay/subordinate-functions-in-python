def Sort_int_number(number):
    num = str(number)
    list = [int(num[i]) for i in range(len(num))]       #making list because 'str' object does not support item assignment
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    sorted_number=''
    for x in list:
        sorted_number+=str(x)
    return sorted_number

number = 4435481348
sorted_number = Sort_int_number(number)
print(sorted_number)

