import tkinter as tk

CELL_SIZE = 20
ROWS, COLS = 20, 20
ERASER_SIZE = 40

def erase(event):
    x, y = event.x, event.y
    for row in range(ROWS):
        for col in range(COLS):
            cell_x1, cell_y1 = col * CELL_SIZE, row * CELL_SIZE
            cell_x2, cell_y2 = cell_x1 + CELL_SIZE, cell_y1 + CELL_SIZE
            if (x - ERASER_SIZE // 2 < cell_x2 and x + ERASER_SIZE // 2 > cell_x1 and
                y - ERASER_SIZE // 2 < cell_y2 and y + ERASER_SIZE // 2 > cell_y1):
                canvas.itemconfig(grid[row][col], fill="white")

root = tk.Tk()
root.title("Canvas Eraser")
canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="white")
canvas.pack()

grid = []
for row in range(ROWS):
    row_cells = []
    for col in range(COLS):
        cell = canvas.create_rectangle(col * CELL_SIZE, row * CELL_SIZE,
                                       (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE,
                                       fill="blue", outline="black")
        row_cells.append(cell)
    grid.append(row_cells)

canvas.bind("<B1-Motion>", erase)  
root.mainloop()