
#WAP TO PRINT YHE VALUE OF LIST  WHICH ARE DIVISIBLE BY 4 AND 8
#l=[10,20,30,40,16,8,4,64]
# for i in l:
#     if i%4==0 and i%8==0 :
#         print(i)


# OUTPUT:
# 40
# 16
# 8
# 64

# WAP TO DISPLAY LIST ELEMENTS OF A LIST
#ALONG WITH +VE ND -VE INDEX

l=[10,20,30,40,50,]
n=len(l)
for i in range(n):
    print("{}present at the index :{} / {}".format(l[i],i,i-n))