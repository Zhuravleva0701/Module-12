
#найти максимальное значение в списке
#def find_max(list_):
#    max_ = list_[0]
#    for i in list_:
#        if i > max_:
#          max_ = i
#    return max_


#print(find_max ([3, 15, 57, 5, 38]))

#подсчет четных чисел в списке

#def count_even(list_):
#    counter = 0
#    for i in list_:
#        if i == 0:
#            continue
#        if i % 2 == 0:
#           counter += 1
#    return counter

#print(count_even([3, 5, 8, 9, 0, 15, 67, 88]))

# уникальный список
def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list

print(unique([2, 13, 56, 7, 8, 3, 2, 4, 4, 4, 8, 8]))


