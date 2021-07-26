from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        islands = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        def validSquare(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                return True
            return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    stack = [(i, j)]
                    islands += 1
                    while stack:
                        cord = stack.pop()
                        visited[cord] = 1
                        for k in range(len(dx)):
                            x = cord[0] + dx[k]
                            y = cord[1] + dy[k]
                            if validSquare(x, y) and (x, y) not in visited and grid[x][y] == '1':
                                stack.append((x, y))
        return islands
