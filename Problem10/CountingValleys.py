def countingValleys(steps, path):
    # Write your code here
    number_of_valley=0
    valley=False
    level=0
    for i in range(0,steps):
        if path[i]=='U':
            level=level+1
        else:
            level=level-1
        if valley==False and level<0:
            number_of_valley = number_of_valley+1
            valley=True
        if level>=0:
            valley=False
    return number_of_valley
            

steps = 8
path = 'DDUUUUDD'
result = countingValleys(steps, path)
print(result)
