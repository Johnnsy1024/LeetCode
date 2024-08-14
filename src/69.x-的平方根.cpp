#include <iostream>
class Solution {
public:
    int mySqrt(int x)
    {
        if (x == 0 | x == 1) {
            return x;
        }
        int left = 1;
        int right = x;
        while (right - left > 1) {
            int middle = left + (right - left) / 2;
            long long tmp = (long long)middle * middle;
            if (tmp > x) {
                right = middle;
            } else if (tmp < x) {
                left = middle;
            } else {
                return middle;
            }
        }
        return left;
    }
};

int main()
{
    int x = 5;
    Solution s;
    std::cout << s.mySqrt(x) << std::endl;
    return 0;
}