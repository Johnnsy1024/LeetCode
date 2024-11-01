from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 1:
            return s
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)  # Output: ["o", "l", "l", "e", "h"]
