class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            if n in record:
                return False
            else:
                record.add(n)

    def get_sum(self, n):
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n = n // 10
        return sum


if __name__ == "__main__":
    print(Solution().isHappy(19))
