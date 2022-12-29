# n = int(input("Enter size of List: "))

# list = []

# for i in range(n):
#     item =input()
#     list.append(item)
    
# print(list)

# Python3 code to Check for
# balanced parentheses in an expression


open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(myStr):
	stack = []
	for i in myStr:
		if i in open_list:
			stack.append(i)
		elif i in close_list:
			pos = close_list.index(i)
			if ((len(stack) > 0) and
				(open_list[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return "No"
	if len(stack) == 0:
		return "Yes"
	else:
		return "No"


# Driver code

n = int(input("Enter size of List: "))

list = []

for i in range(n):
    item =input()
    list.append(item)
    
print(list)

for i in list:
    print(check(i))



# string = "{[]{()}}"
# print(string,"-", check(string))

# string = "[{}{})(]"
# print(string,"-", check(string))

# string = "((()"
# print(string,"-",check(string))

