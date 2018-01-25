print('hello')
def findmatch(n):
    res=[]
    for i in range(2,n):
        bell=bell_number(i)
        for u in range(n):
            for w in range(u+1):
                if (stirling_number2(u,w)==bell):
                    res.append([i,u,w])
    return res
