# phy=int(input('enter the phy value'))
# chem=int(input('enter the chem value'))
# math=int(input('enter the math value'))
# bio=int(input('enter the bio value'))
# it=int(input('enter the it value'))
# eng=int(input('enter the eng value'))
# totalmark=phy+chem+math+bio+it+eng

# avgmark=totalmark/6
# print(totalmark)
# print(avgmark)

# if avgmark>=90 :
#     print('O')
# elif avgmark>=80 and avgmark<=89 :
#     print('E')
# elif avgmark>=70 and avgmark<=79 :
#     print('A')
# elif avgmark>=60 and avgmark<=69 :
#     print('B')
# elif avgmark>=50 and avgmark<=59 :
#     print('C')
# elif avgmark>=40 and avgmark<=49 :
#     print('D')
# else :
#     print('fail better luck next time')

import math
x=int(input('enter x value'))
n=int(input('enter n value'))
if n==1 :
    y=1+x
elif n==2 :
    y=1+(x/n)
elif n==3 :
    y=1+math.pow(x,n)
else :
    y=1+(n*x)
print('y value is :',y)