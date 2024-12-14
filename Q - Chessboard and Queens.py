# def solve(board, row, occupiedCol, occupiedPrimary, occupiedSecondary, ans):
#     if row == 8:
#         ans[0] += 1
#         return
#     for col in range(8):
#         if board[row][col] == '*' or occupiedCol[col] or occupiedPrimary[row - col + 8] or occupiedSecondary[row + col]:
#             continue
#         occupiedCol[col] = occupiedPrimary[row - col + 8] = occupiedSecondary[row + col] = True
#         solve(board, row + 1, occupiedCol, occupiedPrimary, occupiedSecondary, ans)
#         occupiedCol[col] = occupiedPrimary[row - col + 8] = occupiedSecondary[row + col] = False

# board = []
# for i in range(8):
#     board.append(input())

# occupiedCol = [False] * 10
# occupiedPrimary = [False] * 20
# occupiedSecondary = [False] * 20
# ans = [0]
# print(solve(board,0,occupiedCol,occupiedPrimary,occupiedSecondary,ans))