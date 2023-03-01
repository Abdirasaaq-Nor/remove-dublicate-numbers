a = [1,2,3,3,4,5,2,6,7,8,9,6]         #range(1,20)
b=  [] #list(range(1,10))
for i in a:
    if i in b:
        print(f'{i} is dublicate')
        i += 1
    
    else:
        b.append(i)
        i += len(a)
print(b)