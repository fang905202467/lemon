# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} * {} = {}" .format(j,i,j*i),end="\t")
#     print()

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("{} * {} = {}" .format(j,i,j*i),end="\t")
        j += 1
    print()
    i += 1