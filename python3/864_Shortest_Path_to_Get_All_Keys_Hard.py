# 864. Shortest Path to Get All Keys - Hard

class Solution:
    def __init__(self):
        self.Rows = 0
        self.Cols = 0
        self.Grid = None

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        self.Rows = len(grid)
        self.Cols = len(grid[0])
        self.Grid = grid

        start = []
        key_count = 0
        for i in range(self.Rows):
            for j in range(self.Cols):
                letter = grid[i][j]
                if letter == "@":
                    start = [i,j]
                elif letter.islower():
                    key_count += 1

        queue = collections.deque()
        seen = collections.defaultdict(set)

        # [row, column, key_state, cost]
        queue.append((start[0], start[1], 0, 0))
        seen[0].add((start[0], start[1]))

        # BFS
        # With Breadth-First Search algorithms, we can assume costs are
        # the same for the queue entries at the same level. Therefore, if
        # we find the first critical state that has all bits filled, it
        # means that the step is the exact cost we are looking for.
        while queue:
            x, y, keys, cost = queue.popleft()
            # print(x, y, keys, cost)
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                new_x, new_y = x + dx, y + dy

                if 0 <= new_x < self.Rows and 0 <= new_y < self.Cols:
                    letter = self.Grid[new_x][new_y]
                    if letter == "#":
                        continue

                    if letter.islower() and not (1 << (ord(letter) - ord('a'))) & keys:
                        new_keys = (1 << (ord(letter) - ord('a'))) | keys
                        if new_keys == ((1 << key_count) - 1):
                            return cost + 1

                        seen[new_keys].add((new_x, new_y))
                        queue.append((new_x, new_y, new_keys, cost + 1))

                    elif letter.isupper() and not (1 << (ord(letter)) - ord('A')) & keys:
                        continue
                    elif (new_x, new_y) not in seen[keys]:
                        seen[keys].add((new_x, new_y))
                        queue.append((new_x, new_y, keys, cost + 1))

        return -1