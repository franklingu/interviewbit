'''
Write a program to validate if the input string has redundant braces?
Return 0/1

0 -> NO
1 -> YES
Input will be always a valid expression

and operators allowed are only + , * , - , /

Example:

((a + b)) has redundant braces so answer will be 1
(a + (a + b)) doesn't have have any redundant braces so answer will be 0
'''


class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stk = []
        for c in A:
            if c == '(':
                stk.append(c)
            elif c in set('+-*/'):
                if stk:
                    stk.pop()
        if len(stk) > 0:
            return 1
        return 0
