a=[10,20,30,40]
# b=bytes(a)
# print(b[1])
# print(b[3])
# print(b[-2])#backward
# print(b[4])


#bytes arry

b=bytearray(a)
print(b[1])
print(b[3])
print(b[-2])#backward
print(b[4])

b[-1]=50# we can modify the index value
for i in b :
    print(i)
