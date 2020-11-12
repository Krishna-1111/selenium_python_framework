import csv

a = open("testdata_t1.csv", 'r')
#
# b = a.readline()
# print(b)
# # c = a.readlines()
# # print(c)
# d = a.read()
#
#
#
# print(d)

# e = []
# for line in c:
#     e.append([line.strip("\n")])
#     print(e)
b = csv.reader(a)


print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# b = a.read()
# print(a)
# print(next(b))
# for i in range(3):
#     print(next(b))
print(next(b))
# for i in range(3):
#     print(next(b))
    # print(next(b))
    # print(next(b))

