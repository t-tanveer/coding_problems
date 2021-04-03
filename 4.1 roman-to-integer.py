class Solution:
    def romanToInt(self, s: str) -> int:

        romans = { 
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        summation = 0
        index = 0
        while index < len(s):
            if (index != len(s)-1 and romans[s[index+1]] <= romans[s[index]]):
                summation += romans[s[index]]
                # print("[1]/ adding ", romans[s[index]], "to ", summation, "for the index of ", index, "// summation is: ", summation)
            elif index != len(s)-1:
                summation += romans[s[index+1]] - romans[s[index]]
                # print("[2]/ adding ", romans[s[index]], "to ", summation, "for the index of ", index, "// summation is: ", summation)
                index+=1
            elif index == len(s)-1:
                summation+=romans[s[index]]
                # print("3/ adding ", romans[s[index]], "to ", summation, "for the index of ", index, "// summation is: ", summation)
            index+=1
            
        return summation

# Could probably be refactored a bit more meh
            
