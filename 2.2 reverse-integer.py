class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        ans = 0

        if x < -2147483648 or x > 2147483647:
            return 0
        else:
            r = x

            if x < 0:
                r = -1 * r

            for i in range(len(str(x))):

                if r is not 0:
                    ans = ans*10 + r%10
                    r = int (r / 10)

            if x < 0:
                ans = -1 * ans

        if ans < -2147483648 or ans > 2147483647:
            return 0
        return ans
        
#Runtime: 32 ms, faster than 67.95% of Python3 online submissions for Reverse Integer.
#Memory Usage: 14.3 MB, less than 46.71% of Python3 online submissions for Reverse Integer.
