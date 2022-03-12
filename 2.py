num = 0
zero2 = 0
list_finish = []

num1 = 1
num2 = 2

list_finish.append(num1)
list_finish.append(num2)

while zero2 == 0:

    num = num1 + num2
    if num < 4000000:
        list_finish.append(num)
    else:
        break

    num1 = num2
    num2 = num

    if num % 2 !=0:
        list_finish.remove(num)

list_finish.remove(1)

print(sum(list_finish))