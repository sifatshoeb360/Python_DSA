import time

# print(time.strptime('%y'))

x = 4

match x:
    case 0:
        print("case",x)
    case 1:
        print("case",x)
    case _:
        print("default")