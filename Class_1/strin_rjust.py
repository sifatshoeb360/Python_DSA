# WELCOME        TO
#   DEPARTMENT OF CSE
#         AT UGV

mystr = "WELCOME        TO"
mystr2 = "DEPARTMENT OF CSE"
# print(mystr.split())
mx=0;
arr = []
arr.append(mystr.split())
arr.append(mystr2.split())
# print(arr)
for i in arr:
    for j in i:
        print(j,end=" ")
    print()

