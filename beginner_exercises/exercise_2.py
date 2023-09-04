for x in range(10):
    if x == 0:
        print('Current number',x,'Previous number',x,'Sum:',x+x)
        continue
    print("Current number",x,"Previous number",x-1,"Sum:",x+(x-1))
