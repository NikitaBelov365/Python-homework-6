list_input = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
limit = [6, 10]
new_list = []
for i in range(len(list_input)):
    if list_input[i] > limit[0] and i < limit[1]:
        new_list.append(i)
print(new_list)