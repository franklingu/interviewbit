'''
Given a string,
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
'''


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        track = dict()
        mm = 0
        for i, a in enumerate(A):
            if a in track:
                to_remove = set()
                for k, v in track.iteritems():
                    if v <= track[a]:
                        to_remove.add(k)
                track = dict((k, v) for k, v in track.iteritems() if k not in to_remove)
                track[a] = i
                continue
            track[a] = i
            mm = max(mm, len(track))
        return mm
