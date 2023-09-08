def oddeven(*a):
    odd=[]
    even=[]
    for i in a:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
print(oddeven(1,2,3,4,5,6,7,8,9,10))