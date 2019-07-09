'''
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
1 is read off as one 1 or 11.
11 is read off as two 1s or 21.

21 is read off as one 2, then one 1 or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

Example:

if n = 2,
the sequence is 11.
'''

'''
Just code the problem description
'''


class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        s = ['1']
        while A > 1:
            t = []
            count, prev = 0, None
            for c in s:
                if prev is None:
                    prev = c
                    count = 1
                    continue
                if prev == c:
                    count += 1
                else:
                    t.extend(list(str(count)))
                    t.append(prev)
                    count = 1
                    prev = c
            if count > 0:
                t.extend(list(str(count)))
                t.append(c)
            s = t
            A -= 1
        return ''.join(s)
