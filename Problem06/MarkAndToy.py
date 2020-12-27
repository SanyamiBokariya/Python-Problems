def maximumToys(prices, k):
    prices.sort()
    total_cost=0
    count=0
    for i in range(0,len(prices)):
        tc = total_cost + prices[i]
        if tc<=k:
            total_cost=tc
            count=count+1
        else:
            break
    print(count)
    
 maximumToys([1,2,3,4],7)   
