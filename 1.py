first_element = int(input('input first element: '))
difference = int(input('input difference: '))
ammount_of_elements = int(input('input ammount of elements: '))

pgrs = []
pgrs.append(first_element)
for i in range(1, ammount_of_elements):
    pgrs.append(first_element + difference*i)
print(pgrs)  