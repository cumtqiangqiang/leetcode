'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''


def lengthOfLongestSubstring(s: str) -> int:
    sub = ""
    maxLen = 0
    subLen = 0
    for ch in s:
        if ch in sub:
            index = sub.index(ch)
            sub = sub[index + 1:]
            subLen = len(sub)

        sub += ch
        subLen += 1
        if maxLen > subLen:
               maxLen = subLen

    return  maxLen





def otherLengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    sub = ""
    max_len = cur_len = 0

    for ch in s:
        if ch in sub:
            index = sub.index(ch)
            sub = sub[index + 1:]
            cur_len = len(sub)
        sub += ch
        cur_len += 1
        if max_len < cur_len:
            max_len = cur_len
    print(max_len)
    return max_len


if __name__ == '__main__':
    lengthOfLongestSubstring("abcdaef")

    # otherLengthOfLongestSubstring("abcdaef")
