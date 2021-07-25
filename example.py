import divisiblelist as dl

my_list = dl.DivisibleList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

for sublist in my_list / 2:
    print(sublist)

