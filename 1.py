import time
start = time.time()

three = 0
five = 0
three_list = []
five_list = []
steps = 1000
steps3 = steps-3
steps5 = steps-5

while three < steps3:
    three = three+3
    three_list.append(three)

print('\n')

while five < steps5:
    five = five+5
    five_list.append(five)


finish_list = set(three_list+five_list)


print(sum(finish_list))

stop = time.time()-start
print(stop)