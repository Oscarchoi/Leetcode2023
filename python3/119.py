# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []
        for i in range(rowIndex+1):
            row.append(1)
            for j in reversed(range(1,i)):
                row[j] = row[j-1] + row[j]
        return row
