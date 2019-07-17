'''
You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
'''


class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        if len(B) < 0:
            return []
        import itertools
        l = len(B) * len(B[0])
        if l > len(A):
            return []
        possibles = set((''.join(s) for s in itertools.permutations(B)))
        ret = []
        for i, c in enumerate(A):
            if i + l > len(A):
                break
            ss = A[i:i + l]
            if ss in possibles:
                ret.append(i)
        return ret

    def findSubstring2(self, A, B):
        if len(B) < 0:
            return []
        l1 = len(B[0])
        l = len(B) * l1
        if l > len(A):
            return []
        ret = []
        track = dict()
        for s in B:
            if s not in track:
                track[s] = 0
            track[s] += 1
        for i, c in enumerate(A):
            if i + l > len(A):
                break
            start = 0
            tmp = dict(track)
            while start < l:
                s = A[i + start:i + start + l1]
                if s not in tmp:
                    break
                elif tmp[s] <= 0:
                    break
                tmp[s] -= 1
                start += l1
            else:
                ret.append(i)
        return ret
