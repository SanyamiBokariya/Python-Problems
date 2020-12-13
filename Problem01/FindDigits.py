def findDigits(number):
    string=str(number)
    count=0
    for i in range(len(string)):
        if string[i] != '0':
            if number%int(string[i])==0:
                count=count+1
    return count
    
findDigits(10)
