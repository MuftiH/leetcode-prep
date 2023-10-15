from typing import List, Set

"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1: 

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows and cols
        for i in range(len(board)):
            row: Set[str] = set()
            col: Set[str] = set()
            box: Set[str] = set()
            for j in range(len(board[i])):
                box_i: int = ((3*i) + (j // 3)) % 9
                box_j: int = (j % 3) + (3*(i // 3))
                if board[i][j] in row and board[i][j] != ".":
                    return False
                if board[j][i] in col and board[j][i] != ".":
                    return False
                if board[box_i][box_j] in box and board[box_i][box_j] != ".":
                    return False
                row.add(board[i][j])
                col.add(board[j][i])
                box.add(board[box_i][box_j])
        return True