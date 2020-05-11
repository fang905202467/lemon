one_list = []
for i in range(1,101):
    if ('7' not in str(i)) and (i % 7 != 0):
        one_list.append(i)
print(one_list)