class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []

        if numRows == 0:
            return res

        # numRows > 0
        res.append([1])

        for i in range(1, numRows):
            prev_row = res[i - 1]
            row = []

            row.append(1)

            for j in range(0, i - 1):
                row.append((prev_row[j] + prev_row[j + 1]))

            row.append(1)

            res.append(row)

        return res
