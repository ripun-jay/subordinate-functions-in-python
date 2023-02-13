def sort_list(list):
    for i in range(len(list)):                           #using double loop to make tree node which connects to multiple node
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

order = [56,58,23,69,65.2]
sort_order = sort_list(order)
print(sort_order)