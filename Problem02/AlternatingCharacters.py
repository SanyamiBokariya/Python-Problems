def alternatingCharacters(s):
    no_of_characters_to_delete=0
    last_element=s[0]
    for i in range(1,len(s)):
        if s[i]==last_element:
            no_of_characters_to_delete=no_of_characters_to_delete+1
        last_element = s[i]
    return no_of_characters_to_delete 
    
alternatingCharacters('AABAAB')
