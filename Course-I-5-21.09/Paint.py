import tkinter as tk


def paint(event):
    x, y, = event.x, event.y
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill='black', outline='black')


root = tk.Tk()
root.title('Програма за рисуване')
root.geometry('600x600')

canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)
canvas.bind('<B1-Motion>', paint)

root.mainloop()
