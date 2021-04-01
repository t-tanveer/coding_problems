class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if (int(x) < 0):
            x = x*-1
            string_int = (str(x))[::-1]
            int_final = int(string_int)*-1
        else:
            string_int = (str(x))[::-1]
            int_final = int(string_int)

        min_int = (-2**31)
        max_int = (2**31 -1)
        
        
        if not min_int <= int_final <= max_int: 
            return 0
        else:
            return int_final      
            
#Runtime: 32 ms, faster than 67.95% of Python3 online submissions for Reverse Integer.
#Memory Usage: 14.2 MB, less than 46.71% of Python3 online submissions for Reverse Integer. 
