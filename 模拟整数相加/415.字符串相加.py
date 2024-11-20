class Solution:
    """给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回"""

    def addStrings(self, num1: str, num2: str) -> str:
        d1 = len(num1) - 1
        d2 = len(num2) - 1
        carry = 0
        sum = []

        while d1 >= 0 or d2 >= 0 or carry > 0:
            # 该边界条件表示的是：两个数逐位相加还没有完全遍历完,就算原本两数各自的位数都算完了,进位没到0也不退出计算
            if d1 >= 0:
                temp1 = int(num1[d1])
            else:
                temp1 = 0
            d1 -= 1
            if d2 >= 0:
                temp2 = int(num2[d2])
            else:
                temp2 = 0
            d2 -= 1
            sum.append(f"{(temp1 + temp2 + carry) % 10}")
            carry = (temp1 + temp2 + carry) // 10
        return "".join(sum[::-1])
