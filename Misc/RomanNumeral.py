def romanToInt(s: str) -> int:
    romanMap = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
    result = 0
    for i in range(len(s)-1, -1, -1):    
        thisNum = romanMap[s[i]]
        
        if i < len(s)-1:
            prevNum = romanMap[s[i+1]]
            if thisNum < prevNum:
                result -= thisNum
            else:
                result += thisNum
        else:
            result += thisNum
        
    return result
            
print( romanToInt('MMXXII') )
