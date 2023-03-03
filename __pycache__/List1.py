# l=[10,20,30,'soumya',5.6]
# print(l)
# print(l[-2])
# print(l[4])

#==============================
#CREATION OF EMPTY LIST

# l=[]
# print(l)
#==============================

#==============================
#creation of list by using eval()

# l=eval(input("enter a list"))
# print(l)

#OUTPUT
# enter a list[10,20,30,40]
# [10, 20, 30, 40]
#===============================

#==============================
#CREATION OF LIST USING LIST()
# l=list((23,33,43,53,63))
# print(l)

# OUTPUT
# [23, 33, 43, 53, 63]
# =================================

#========================================
#CREATION OF LIST USING RANGE()

# l=list(range(10,21))
# print(l)

# OUTPUT
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# =============================================

# ===================================
# #CREATION OF LIST DIRECTLY

# l=[10,20,30,'soumya',True,9.9]
# print(l)

# OUTPUT
# [10, 20, 30, 'soumya', True, 9.9] 
# ===================================

# ===================================================
# LIST HOLD COMPLEX DATATYPE

# l=[23,{"name":"soumya"},list((10,20,30,40))]
# print(l)
# OUTPUT
# [23, {'name': 'soumya'}, [10, 20, 30, 40]]
# ===================================================

# =====================================
# CREATION OF LIST BY USING SPLIT()
# EXAMPLE-1

# msg="hii welcome to python"
# l=msg.split()
# print(l)

# OUTPUT
# ['hii', 'welcome', 'to', 'python'] 
# =====================================
# ==========================================================
# EXAMPLE-2
# msg="welc-ome- t-o py-tho-n cl-ass"
# l=msg.split('-')
# print(l)

# OUTPUT
# ['welc', 'ome', ' t', 'o py', 'tho', 'n cl', 'ass']
# =========================================================

# ===============================================
# # EXAMPLE-3
# msg="welc-ome- t-o py-tho-n cl-ass"
# l=msg.split('o')
# print(l)
# OUTPUT
# ['welc-', 'me- t-', 
# ' py-th', '-n cl-ass']
# =================================================