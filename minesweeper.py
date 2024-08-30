def minesweeper(board):
    rows = len(board)
    cols = len(board[0])
    final_board = [[0]*cols for _ in range(rows)]
    
    # Directions for all 8 neighbors (up, down, left, right, and diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 1:
                final_board[r][c] = 9
            else:
                # count numbers of mines around the cell
                mine_count = 0
                for dr, dc in directions:
                    # Moving inside de board
                    nr, nc = r + dr, c + dc
                    # If it is inside the board and the is a mine count it
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 1:
                        mine_count += 1
                final_board[r][c] = mine_count
    return final_board
    
    
if __name__ == "__main__":
    board = [
    [1, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 0]
    ]
    result = minesweeper(board)
    for x in range (0,len(result)):
        print(result[x])
