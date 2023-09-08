def a(*m):
    result=0
    for i in m:
        result=result+i
    return result
print(a(2,3,4))