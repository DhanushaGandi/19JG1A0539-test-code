def occ(str1,str2):
    s=str2[-1]
    count=0
    for i in str1:
        if i==s:
            count=count+1
    return count
str1=input()
str2=input()
print(occ(str1,str2))
        
    
