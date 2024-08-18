#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix)
    {
        if (matrix.empty())
            return {};

        int rowNum = matrix.size();
        int colNum = matrix[0].size();
        int startX = 0, startY = 0;
        vector<int> res;

        while (rowNum > 0 && colNum > 0) {
            // If there's only one row/column left, add them all
            if (rowNum == 1) {
                for (int j = 0; j < colNum; j++) {
                    res.push_back(matrix[startX][startY + j]);
                }
                break;
            } else if (colNum == 1) {
                for (int i = 0; i < rowNum; i++) {
                    res.push_back(matrix[startX + i][startY]);
                }
                break;
            }

            // Top row
            for (int j = 0; j < colNum - 1; j++) {
                res.push_back(matrix[startX][startY + j]);
            }
            // Right column
            for (int i = 0; i < rowNum - 1; i++) {
                res.push_back(matrix[startX + i][startY + colNum - 1]);
            }
            // Bottom row
            for (int j = colNum - 1; j > 0; j--) {
                res.push_back(matrix[startX + rowNum - 1][startY + j]);
            }
            // Left column
            for (int i = rowNum - 1; i > 0; i--) {
                res.push_back(matrix[startX + i][startY]);
            }

            startX++;
            startY++;
            rowNum -= 2;
            colNum -= 2;
        }

        return res;
    }
};

int main()
{
    Solution s;
    vector<vector<int>> matrix = { { 6, 9, 7 } };
    vector<int> res;
    res = s.spiralOrder(matrix);
    for (auto& x : res) {
        cout << x << " ";
    }
}