'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Your program should return a list of strings, where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
 Note: Each word is guaranteed not to exceed L in length.
'''


class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        def justify(A, start, end, num):
            ret = []
            if end == start:
                ret.append(A[start])
                if num > 0:
                    ret.append(' ' * num)
                return ''.join(ret)
            avg, remainder = divmod(num, end - start)
            for i in xrange(start, end + 1):
                w = A[i]
                if not w:
                    continue
                ret.append(w)
                if remainder > 0:
                    ret.append(' ' * (avg + 1))
                    remainder -= 1
                elif i == end:
                    break
                else:
                    ret.append(' ' * (avg))
            return ''.join(ret)

        ret = []
        acc = 0
        start = 0
        empty = 0
        for i, w in enumerate(A):
            l = len(w)
            if l == 0:
                empty += 1
                continue
            if acc + l + (i - start) > B:
                ret.append(justify(A, start, i - 1, B - acc - empty))
                empty = 0
                start = i
                acc = l
            else:
                acc += l
        tmp = []
        acc = 0
        for i in xrange(start, len(A)):
            if not A[i]:
                continue
            tmp.append(A[i])
            acc += len(A[i])
            if acc < B:
                tmp.append(' ')
                acc += 1
        if acc > 0:
            tmp.append(' ' * (B - acc))
        ret.append(''.join(tmp))
        return [s for s in ret if s]
