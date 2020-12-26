from collections import Counter

# Complete the isValid function below.
def isValid(s):
    c = Counter(Counter(s).values())
    if len(c)==1:
        return "YES"
    elif len(c)>2:
        return "NO"
    elif 1 in c.values() and (c[min(c.keys())]==1 or (max(c.keys()) - min(c.keys())==1)):
        return "YES"
    else:
        return "NO"
        
 isValid('aabbccc')
