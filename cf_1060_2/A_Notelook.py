def min_protections(n, k, s):
    ans=0
    j=0
    flag=True
    for i in range(n):
        if s[i]=='1' and flag==False:
            if i-j>k-1:
                ans+=1
                j=i
            else:
                j=i
        elif s[i]=='1' and flag==True:
            ans+=1
            flag=False
            j=i
            
    return ans
              
         

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = list(input().strip())
    print(min_protections(n, k, s))
