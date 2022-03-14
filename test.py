import time
start = time.time()

txt = '''import time
start = time.time()



stop = time.time()-start
print(stop)'''

a = [i for i in range(4,100)]

# for key in a:
#     my_file = open(str(key) + '.py', "w+")
#     my_file.write(txt)
#     my_file.close()

stop = time.time()-start

print(stop)