def jumpingOnClouds(c):
    n=len(c)
    count=0
    i=0
    while i < n: 
        if c[i] != 1 and i+2 < n and c[i+2] != 1:
            count = count + 1
            i = i+2
        elif c[i] != 1 and i+1 < n and c[i+1] !=1:
            count = count + 1
            i=i+1
        else:
            i=i+1
    return count
        
n = 7
c = [0,0,1,0,0,1,0]

result = jumpingOnClouds(c)
print(result)
