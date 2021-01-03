
class Simulation:
    def __init__(self, path):
        self.grid = []
        self.seat_check = [
            (-1,-1),(0,-1),(1,-1),
            (-1,0),        (1,0),
            (-1,1), (0,1), (1,1)
        ]

        with open(path) as f:
            self.grid = [list(l.strip()) for l in f.readlines()]

    def step(self):
        changes_made = False

        # make a copy of the grid
        new_grid = []
        for gl in self.grid:
            new_grid.append(list(gl))

        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                changes_made |= self.updateSeat(self.grid, new_grid, row, col)

        self.grid = new_grid
        
        return changes_made

    def run(self):
        while self.step():
            pass

    # Returns True if the seat value has changed
    def updateSeat(self, old_grid, new_grid, row, col):
        if old_grid[row][col] == '.':
            return False

        occupied_seats = 0
        height = len(old_grid)
        width = len(old_grid[0])

        for rd, cd in self.seat_check:
            r = row + rd
            c = col + cd
            if r >= 0 and r < height and c >= 0 and c < width:
                if old_grid[r][c] == '#':
                    occupied_seats += 1
        
        if occupied_seats >= 4 and old_grid[row][col] == '#':
            new_grid[row][col] = 'L'
            return True
        elif occupied_seats == 0 and new_grid[row][col] == 'L':
            new_grid[row][col] = '#'
            return True
        return False

    def print(self):
        for gl in self.grid:
            print(gl)

    def occupied(self):
        count = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == '#':
                    count += 1
        return count

s = Simulation('2020/day11/input')
s.run()
print(s.occupied())