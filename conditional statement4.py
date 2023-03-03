# WAP ,INPUT 2 NUMBER PERFORM CALCULATION BASED ON USER INPUT (ADD,SUB,MUL,DIV)

# a=int(input('enter a value'))
# b=int(input('enter b value'))

# ch=input('enter choice \n add \n sub \n mul \n div \n ')

# if ch=='add' :
#     print(a+b)
# elif ch=='sub' :
#     print(a-b)
# elif ch=='mul' :
#     print(a*b)
# elif ch=='div' :
#     print(a/b)
# else :
#     print('invalid option')


sal=int(input('enter ur salary'))
gen=input('enter ur gender')
if gen =='male' :
    bonous=0.05*sal
else :
    bomous=0.10*sal

if sal<1500 :
    bonous=bonous+0.03*sal

sal=bonous+sal
print('salary is',sal)