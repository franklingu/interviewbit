'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given “25525511135”,

return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
'''

'''
Back tracking problem
'''


class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        def isValidIPFragment(s):
            val = int(s)
            if not (0 <= val <= 255):
                return False
            if len(s) > 1 and s[0] == '0':
                return False
            return True

        def findValidIPs(A, res, curr, pos):
            if pos == 3:
                if isValidIPFragment(A[curr[-1] + 1:]):
                    res.append(curr)
                return
            if pos == 0:
                start = 0
            else:
                start = curr[pos - 1] + 1
            for i in xrange(start, len(A) - 3 + pos):
                isValid = isValidIPFragment(A[start:i + 1])
                if not isValid:
                    continue
                curr = list(curr)
                curr[pos] = i
                findValidIPs(A, res, curr, pos + 1)

        def translateIntoIP(A, ls):
            ls = set(ls)
            ret = []
            for i, e in enumerate(A):
                ret.append(e)
                if i in ls:
                    ret.append('.')
            return ''.join(ret)

        if len(A) > 12:
            return []
        res = []
        curr = [0, 0, 0]
        findValidIPs(A, res, curr, 0)
        return [translateIntoIP(A, ls) for ls in res]
