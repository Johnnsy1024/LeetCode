/*
 * @lc app=leetcode.cn id=59 lang=cpp
 *
 * [59] 螺旋矩阵 II
 */
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n)
    {
        vector<vector<int>> res(n, vector<int>(n, 0));
        int loop = n / 2; // n = 3时循环1圈，中间补数字n， n = 4时循环2圈，n = 5时循环2圈，中间补数字n
        int start_x = 0; // 当前轮起始的x坐标
        int start_y = 0; // 当前轮起始的y坐标
        int mid = n / 2; // 中间点的位置（如果n为奇数）
        int cur_num = 1; // 当前要填充到格子里的数字
        int offset = 1; // 当前循环轮离矩阵边缘的偏差距离
        int i, j;
        while (loop) {
            i = start_x;
            j = start_y;

            for (; j < n - offset; j++) {
                res[i][j] = cur_num++;
            }
            for (; i < n - offset; i++) {
                res[i][j] = cur_num++;
            }
            for (; j > start_y; j--) {
                res[i][j] = cur_num++;
            }
            for (; i > start_x; i--) {
                res[i][j] = cur_num++;
            }
            start_x++;
            start_y++;
            loop--;
            offset += 1;
        }
        if (n % 2 == 1) {
            res[mid][mid] = n * n;
        }
        return res;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> res = s.generateMatrix(5);
    for (auto& row : res) {
        for (auto& num : row) {
            cout << num << " ";
        }
        cout << endl;
    }
}