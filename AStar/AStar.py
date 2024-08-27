import heapq

ROW = 9
COL = 9


class Cell:
    def __init__(self, parent_i=0, parent_j=0, f=float("inf"), g=float("inf"), h=0, i=0, j=0, parent=None):
        self.parent_i = parent_i
        self.parent_j = parent_j
        self.parent = parent
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j

    def __lt__(self, other):
        return self.f < other.f

def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5


def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

def is_unblocked(grid, row, col):
    return grid[row][col] == 1

def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

def trace_path(cell, src):
    print("The Path is ")
    path = []

    while cell.parent:
        path.append((cell.i, cell.j))
        cell = cell.parent

    path.append((src[0], src[1]))
    path.reverse()

    for i in path:
        print("->", i, end=" ")
    print()
    return path


def a_star_search(grid, src, dest):
    print("searching...")

    if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
        print("Source or destination is invalid.")
        return

    if not is_unblocked(grid, src[0], src[1]) or not is_unblocked(grid, dest[0], dest[1]):
        print("Source or the destination is an obstacle.")
        return

    if is_destination(src[0], src[1], dest):
        print("We are already at the destination.")
        return

    closed_list = []

    start_cell = Cell(f=0, g=0)
    start_cell.i = src[0]
    start_cell.j = src[1]

    open_list = []
    heapq.heappush(open_list, start_cell)

    found_dest = False

    while open_list:
        p = heapq.heappop(open_list)

        i = p.i
        j = p.j
        closed_list.append((p.i, p.j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                      #(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and (new_i, new_j) not in closed_list:
                cur_cell = Cell(parent_i=i, parent_j=j, i=new_i, j=new_j, parent=p)
                if is_destination(new_i, new_j, dest):
                    txt = "found"
                    path = trace_path(cur_cell, src)
                    found_dest = True
                    return path, txt
                else:
                    g_new = p.g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    if cur_cell.f == float('inf') or cur_cell.f > f_new:
                        heapq.heappush(open_list, cur_cell)
                        cur_cell.f = f_new
                        cur_cell.g = g_new
                        cur_cell.h = h_new
                        cur_cell.parent_i = i
                        cur_cell.parent_j = j
    if not found_dest:
        print("Destination is blocked")
        return "inf", "Failed"

def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    src = [0, 0]
    dest = [6, 7]

    a_star_search(grid, src, dest)


if __name__ == "__main__":
    main()
