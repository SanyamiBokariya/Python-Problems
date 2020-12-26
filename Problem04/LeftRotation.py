def rotLeft(input_array, number_of_rotation):
    a=input_array[number_of_rotation:]
    b=input_array[:number_of_rotation]
    return a+b
    
rotLeft([1,2,3,4,5],2)    
