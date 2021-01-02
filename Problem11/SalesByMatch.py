from collections import Counter

def sockMerchant(n, ar):
        pairs=0
        socks = Counter(ar)
        for s in socks:
            pairs += socks[s]//2
        return pairs

n = 7
ar = [1,2,1,2,1,3,1]
result = sockMerchant(n, ar)
print(result)
