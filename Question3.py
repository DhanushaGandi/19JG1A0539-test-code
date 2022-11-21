validnumbers=['1','2','5','6','8','9','0']
number=int(input())
m=0
kk=[]
for i in range(100):
    for j in str(i):
        if j not in validnumbers:
            break
    else:
        kk.append(i)
        m=m+1
        if m==number+1:
            print(i)
            break  
