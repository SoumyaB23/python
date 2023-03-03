# PRINT YOUR NME 10 TIMES

# i=1

# while i<=10 :
#     print('soumyaranjan baral')
#     i=i+1

# PRINT THE NUMBER 1 TO 10

# i=1

# while i<=10 :
#     print(i)
#     i=i+1

# PRINT THE NUMBER 90 TO 100

# i=90
# while i<=100 :
#     print(i)
#     i=i+1

# PRINT THE NUMBER 10 TO 1

# i=10
# while i>=1 :
#     print(i)
#     i=i-

# PRINT THE NUMBER 999 TO 990
# i=int(input('enter your number'))

# while i>=990 :
#     print(i)
#     i=i-1

# PRINT THE NUMBER SERIES LIKE 111,222,333,444,555,666

# i=111
# while i<=666 :
#     print(i)
#     i=i+111


# PRINT THE NUMBER SERIES LIKE 999,777,555,333

# i=999
# while i>=333 :
#     print(i)
#     i=i-222

# PRINT THE NUMBER 111 TO 120

# i=110
# while i<=120 :
#     print(i)
#     i=i+1

# PRINT THE '*' VERTICALLY 10 TIMES

# i=1
# while i<=10 :
#     print('*')
#     i=i+1

# PRINT THE '*' HORIZONTALY 10 TIMES

# i=1
# while i<=10 :
#     print('*', end='  ')
#     i=i+1

# WAP TO CALCULATE THE SUM OF FIRST 10 DIGITS

# i=1
# result =0
# while i<=10 :
#     result =result+i
#     i=i+1
# print(result)

# WAP TO CALCULATE THE SUM OF NUMBERS FROM M TO N


# m=int(input('enter the m value'))
# n=int(input('enter the n value'))
# sum=0
# while m<=n :
#     sum=sum+m
#     m=m+1
# print('sum is :',sum)

# WAP TO READ THE NUMBERS UNTIL -1 IS ENTERED ALSO COUNT THE NEGATIVE,POSITIVE AND ZEROS ENTERED BY THE USERS
# num=int(input('enter a number (if u want to exit enter -1)'))
# np=0
# nn=0
# nz=0
# while num!= -1 :
#     if num >0:
#         np=np+1
#     elif num<0:
#         nn=nn+1
#     else:
#         nz=nz+1
#     num=int(input('enter a number (if u want to exit enter -1)::'))
# print(np)
# print(nn)
# print(nz)
    
 
# WAP TO DISPLAY MULTIPLICATION  TABLE OF A NUMBER

num = int (input('enter the number '))
i=1
while i<=10 :
    #print(num*i)
    #print(num,'*',i,'=',num*i)
    print(f'{num}*{i}={num*i}')
    i=i+1