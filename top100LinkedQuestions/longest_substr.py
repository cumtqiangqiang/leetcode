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
    dic = {}
    maxL = 0
    start = 0
    for i in range(len(s)):
        letter = s[i]
        if letter not in dic.keys():
            dic[s[i]] = 0
        else:
            diff = i - start
            maxL = diff if diff > maxL else maxL


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
    # lengthOfLongestSubstring("abcdaef")

    otherLengthOfLongestSubstring("abcdaef")
