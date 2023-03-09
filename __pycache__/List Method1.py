#APPEND():
#============
# l=[10,20,30,40,50]
# l.append(456)
# l.append(432)
# print(l)


#WAP TO CREATE A LIST BY ADDIND 20 0'S
# l=[]
# for i in range(20):
#     l.append(0)
# print(l)    

#WAP TO CREATE A LIST BY ADDIND 0 TO 20
# l=[]
# n=21
# for i in range(n):
# #for i in range(21):
#     l.append(i)
# print(l)

#INSERT():
#=========
l=[10,12,43,40,50]
# l.insert(2,543)
# l.insert(1,678)
# print(l)
# print(l.index(678))
# l.insert(6,89)# if the specified +ve number crossed the maximum index then it will behave likeappend()
# print(l)
l.insert(-7,55) 
print(l)
# if the specified -ve index crossed the minimum index the it print at the begining of the list
