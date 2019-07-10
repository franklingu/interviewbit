'''
Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
'''


class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        A = A.split('/')
        stk = []
        for s in A:
            if s == '.' or s == '':
                continue
            elif s == '..':
                if stk:
                    stk.pop()
            else:
                stk.append(s)
        return '/' + '/'.join(stk)
