from typing import List


class Solution:
    def __init__(self) -> None:
        self.__values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.__grid = {}
        self.__hints_rows = {}
        self.__hints_columns = {}
        self.__hints_blocks = {}
        self.__rows = {key: set() for key in range(0, 9)}
        self.__columns = {key: set() for key in range(0, 9)}
        self.__groups = {}

    def solveSudoku(self, board: List[List[str]]) -> None:
        for r in range(3):
            for c in range(3):
                self.__groups[(r, c)] = set()

        hints = []
        for r, row in enumerate(board):
            for c, column in enumerate(row):
                if column == '.':
                    hints.append((c, r))
                    continue
                self.__grid[(c, r)] = column
                self.__rows[r].add(column)
                self.__columns[c].add(column)
                self.__groups[(c // 3, r // 3)].add(column)
        for h in hints:
            if h[0] not in self.__hints_columns:
                self.__hints_columns[h[0]] = {}
            self.__hints_columns[h[0]][h] = []
            if h[1] not in self.__hints_rows:
                self.__hints_rows[h[1]] = {}
            self.__hints_rows[h[1]][h] = []
            b = (h[0] // 3, h[1] // 3)
            if b not in self.__hints_blocks:
                self.__hints_blocks[b] = {}
            self.__hints_blocks[b][h] = []

        while len(self.__grid) < 81:
            print("Scanning...")

            while True:
                self.find_hints()
                if not self.process_singles():
                    break
                self.loop()
                pass

        for cell in self.__grid:
            board[cell[1]][cell[0]] = self.__grid[cell]

    def loop(self):
        self.find_singles_in_rows()
        self.process_singles()
        self.find_singles_in_columns()
        self.process_singles()
        self.find_singles_in_blocks()
        self.process_singles()
        self.find_hidden_pairs_in_blocks()
        self.process_singles()


    # def swordfish(self):

    def find_hidden_pairs_in_blocks(self):
        print("find_hidden_pairs_in_blocks")
        block: dict
        for block in self.__hints_blocks.values():
            hints = self.calculate_hints(block.items())
            hints_with_pairs = {item: details for item, details in hints.items()
                                if details[0] == 2}
            processed = []
            for value, details in hints_with_pairs.items():
                if value in processed:
                    continue
                processed.append(value)
                for value2, details2 in hints_with_pairs.items():
                    if value2 == value:
                        continue
                    if details == details2:
                        processed.append(value2)
                        new_values = [value, value2]
                        self.set_hint(new_values, details[1][0])
                        self.set_hint(new_values, details[1][1])
                        break

    def find_singles_in_blocks(self):
        print("find_singles_in_blocks")
        block: dict
        for block in self.__hints_blocks.values():
            hints = self.calculate_hints(block.items())
            for item, details in hints.items():
                if details[0] == 1:
                    cell = details[1][0]
                    self.add(item, cell[0], cell[1])
                    del block[cell]
                    self.remove_hint_in_row(item, cell[1])
                    self.remove_hint_in_column(item, cell[0])

    def find_singles_in_columns(self):
        print("find_singles_in_columns")
        column: dict
        for column in self.__hints_rows.values():
            hints = self.calculate_hints(column.items())
            for item, details in hints.items():
                if details[0] == 1:
                    c_key = details[1][0]
                    self.add(item, c_key)
                    del column[c_key]
                    self.remove_hint_in_row(item, c_key[1])
                    self.remove_hint_in_block(item, c_key)

    def find_singles_in_rows(self):
        print("find_singles_in_rows")
        row: dict
        for row in self.__hints_rows.values():
            hints = self.calculate_hints(row.items())
            for item, details in hints.items():
                if details[0] == 1:
                    c_key = details[1][0]
                    self.add(item, c_key)
                    del row[c_key]
                    self.remove_hint_in_column(item, c_key[0])
                    self.remove_hint_in_block(item, c_key)

    def calculate_hints(self, values) -> dict:
        hints = {}
        for c_key, cell in values:
            for item in cell:
                if item not in hints:
                    hints[item] = (0, [])
                keys = hints[item][1]
                keys.append(c_key)
                hints[item] = (hints[item][0] + 1, keys)
        return hints
    # def remove_in_hints(self, values: [str], hints: List):

    def remove_hint_in_column(self, value: str, c_key: int):
        for column in self.__hints_columns[c_key].values():
            try:
                column.remove(value)
            except:
                pass

    def remove_hint_in_row(self, value: str, r_key: int):
        for row in self.__hints_rows[r_key].values():
            try:
                row.remove(value)
            except:
                pass

    def remove_hint_in_block(self, value: str, key: tuple):
        for block in self.__hints_blocks[(key[0] // 3, key[1] // 3)].values():
            try:
                block.remove(value)
            except:
                pass

    def findPairsInRows(self):
        hints_rows = {}
        for h in self.__hints:
            if len(self.__hints[h]) != 2 and len(self.__hints[h]) != 3:
                continue
            if h[1] not in hints_rows:
                hints_rows[h[1]] = {}
            s = "".join(self.__hints[h])
            if s not in hints_rows[h[1]]:
                hints_rows[h[1]][s] = (0, [],)
            x = hints_rows[h[1]][s][1]
            x.append(h)
            hints_rows[h[1]][s] = (hints_rows[h[1]][s][0] + 1, x)
        for key, value in hints_rows.items():
            for key2, value2 in value.items():
                if value2[0] == 1:
                    self.__hints[value2[1]] = [key2]

    def findObviousInColumns(self):
        hints_columns = {}
        for h in self.__hints:
            if h[0] not in hints_columns:
                hints_columns[h[0]] = {}
            for hh in self.__hints[h]:
                if hh not in hints_columns[h[0]]:
                    hints_columns[h[0]][hh] = (0, None)
                hints_columns[h[0]][hh] = (hints_columns[h[0]][hh][0] + 1, h)

        for key, value in hints_columns.items():
            for key2, value2 in value.items():
                if value2[0] == 1:
                    self.__hints[value2[1]] = [key2]

    def findObviousInGroups(self):
        hints_groups = {}
        # self.__groups[(cell[0]//3, cell[1]//3)]
        for h in self.__hints:
            k = (h[0] // 3, h[1] // 3)
            if k not in hints_groups:
                hints_groups[k] = {}
            for hh in self.__hints[h]:
                if hh not in hints_groups[k]:
                    hints_groups[k][hh] = (0, None)
                hints_groups[k][hh] = (hints_groups[k][hh][0] + 1, h)

        for key, value in hints_groups.items():
            for key2, value2 in value.items():
                if value2[0] == 1:
                    self.__hints[value2[1]] = [key2]

    def clearHints(self):
        for row in self.__hints_rows.values():
            for cell in row.values():
                cell.clear()
        for column in self.__hints_columns.values():
            for cell in column.values():
                cell.clear()
        for block in self.__hints_blocks.values():
            for cell in block.values():
                cell.clear()

    def find_hints(self):
        self.clearHints()
        cell: List
        for row in self.__hints_rows.values():
            for c_key, cell in row.items():
                for v in self.__values:
                    b_key = (c_key[0] // 3, c_key[1] // 3)
                    if (v not in self.__rows[c_key[1]] and
                            v not in self.__columns[c_key[0]] and
                            v not in self.__groups[b_key]):
                        cell.append(v)
                        self.__hints_columns[c_key[0]][c_key].append(v)
                        self.__hints_blocks[b_key][c_key].append(v)

    def add(self, value, key):
        self.__grid[key] = value
        self.__columns[key[0]].add(value)
        self.__rows[key[1]].add(value)
        self.__groups[(key[0] // 3, key[1] // 3)].add(value)
        print(
            f'Found: ({key[0] + 1}:{key[1] + 1}) {value}')

    def set_hint(self, value, key):
        self.__hints_columns[key[0]][key] = value
        self.__hints_rows[key[1]][key] = value
        self.__hints_blocks[(key[0] // 3, key[1] // 3)][key] = value

    def process_singles(self) -> bool:
        print("process_singles")
        found = False
        hints_to_remove = []
        for row in self.__hints_rows.values():
            for c_key, cell in row.items():
                l: int = len(cell)
                if l == 1:
                    found = True
                    value = cell[0]
                    self.add(value, c_key)
                    hints_to_remove.append(c_key)
        for h in hints_to_remove:
            del self.__hints_columns[h[0]][h]
            del self.__hints_rows[h[1]][h]
            del self.__hints_blocks[(h[0] // 3, h[1] // 3)][h]
        return found

    def removeHints(self, hints_to_remove: List) -> dict:
        return {key: self.__hints[key] for key in self.__hints if
                key not in hints_to_remove}


if __name__ == "__main__":
    # Create an instance of the Solution class
    solution_instance = Solution()
    solution_instance.solveSudoku(
        [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]

    )
