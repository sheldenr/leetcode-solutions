class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        island_count = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= columns:
                return

            if grid[row][col] != '1':
                return


            grid[row][col] = '0'

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    dfs(r, c)
                    island_count += 1

        return island_count
