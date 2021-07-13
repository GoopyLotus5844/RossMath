a, b = 37, 360
i = 1
while(True):
    if(a * i % b == 0): 
        print('done')
        break
    print(a * i % b) 
    i += 1
    