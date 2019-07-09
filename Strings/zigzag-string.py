'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.
'''


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B == 1:
            return A
        triLen = B + B - 2
        ret = []
        for i in xrange(B):
            j = i
            currLen = triLen - i - i
            while j < len(A):
                ret.append(A[j])
                if currLen != triLen and currLen > 0 and j + currLen < len(A):
                    ret.append(A[j + currLen])
                j = j + triLen
        return ''.join(ret)
