'''
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
'''

'''
For characters in the right that are smaller than current character, each
effectively make the rank larger by fact(len(A) - pos).
'''


class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        def fact(n) : 
            f = 1
            while n >= 1 : 
                f = f * n 
                n = n - 1
            return f 
              
        # A utility function to count smaller  
        # characters on right of arr[low] 
        def findSmallerInRight(st, low, high) : 
            countRight = 0
            i = low + 1
            while i <= high : 
                if st[i] < st[low] : 
                    countRight = countRight + 1
                i = i + 1
            return countRight 
              
        # A function to find rank of a string 
        # in all permutations of characters 
        def findRankInner(st) : 
            ln = len(st) 
            mul = fact(ln) 
            rank = 1
            i = 0 
            while i < ln : 
                mul = mul / (ln - i) 
                countRight = findSmallerInRight(st, i, ln-1) 
                rank = rank + countRight * mul
                i = i + 1
            return rank
            
        return findRankInner(A) % 1000003
