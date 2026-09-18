'''
7. Reverse Integer
Medium
Topics
premium lock icon
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        n=x
        while (n!=0):
            if(x<0):
                n=abs(n)
            digit = n%10
            print("digit", digit)
            rev = rev*10 + digit
            n=int(n/10)
            print("x", n)
        if(x<0):
            rev = rev*(-1)
        print(rev)
        return rev
        