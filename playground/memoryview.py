import time
for n in (100000, 200000, 300000, 400000):
    #data = 'x'*n
    data = bytes(n)
    start = time.time()
    b = data
    # print(b)
    while b:
        b = b[1:]
        # print(b)
    print('bytes', n, time.time()-start)

for n in (100000, 200000, 300000, 400000):
    #data = 'x'*n
    data = bytes(n)
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview', n, time.time()-start)

# https://stackoverflow.com/questions/18655648/what-exactly-is-the-point-of-memoryview-in-python

# data = bytes(3)
# print(data)
# b = data
# while b:
#     b = b[1:]
#     print(b)
#     print(type(b))