"""
Description: 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 
字母异位词
Author: Johnnsy Feng
Date: 2024-09-05:13:43:30
LastEditTime: 2024-09-05:13:43:30
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in record:
            if i != 0:
                return False
        return True


if __name__ == "__main__":
    print(Solution().isAnagram("anagram", "nagaram"))
