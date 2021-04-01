class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        if str(x)[::-1] == str(x)[0::]:
            return True
        else:
            return False
#Runtime: 72 ms, faster than 28.45% of Python3 online submissions for Palindrome Number.
#Memory Usage: 14.3 MB, less than 16.93% of Python3 online submissions for Palindrome Number.
