def repeatedString(s, n):
    length=len(s)
    if length < n:
        a=int(n/length)
        b=n%length
        count=0
        for i in range(0,length):
            if 'a' in s[i]:
                count=count+1
        count=count*a
        if b>0:
            s=s[:b+1]
            for i in range(0,b):
                if 'a' in s[i]:
                    count=count+1
        return count
    else:
        count=0
        for i in range(0,n):
            if 'a' in s[i]:
                count=count+1
        return count
        

s = 'abcac'
n = 10
result = repeatedString(s, n)
print(result)
