'''
Given a string s, partition s such that every string of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
*
*
*
(len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
'''


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        def isPalindrome(A, curr, end):
            if len(curr) == 0:
                start = 0
            else:
                start = curr[-1] + 1
            while start < end:
                if A[start] != A[end]:
                    return False
                start += 1
                end -= 1
            return True

        def fillPartitions(A, index, curr, partitions):
            if index >= len(A) - 1:
                ok = isPalindrome(A, curr, index)
                if ok:
                    partitions.append(list(curr) + [index])
                return
            ok = isPalindrome(A, curr, index)
            if ok:
                curr.append(index)
                fillPartitions(A, index + 1, curr, partitions)
                curr.pop()
            fillPartitions(A, index + 1, curr, partitions)

        def getPartitionedParts(A, partitions):
            ret = []
            for ss in partitions:
                if not ss:
                    ret.append([A])
                    continue
                tmp = []
                prev = 0
                for index in ss:
                    tmp.append(A[prev:index + 1])
                    prev = index + 1
                ret.append(tmp)
            return ret

        partitions = []
        fillPartitions(A, 0, [], partitions)
        return getPartitionedParts(A, partitions)
