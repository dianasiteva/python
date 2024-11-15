import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Loading')
root.geometry('1000x1000')
root.configure(bg='black')

loading_label = tk.Label(root, text='Loading [0%]', font=('Helvetica', 14), fg='white', bg='black')
loading_label.pack(pady=80)

skull_image = Image.open('skull.jpg')
skull_photo = ImageTk.PhotoImage(skull_image)

skull_label = tk.Label(root, image=skull_photo, bg='black')
skull_label.pack(pady=80)

i = 0

while i <= 100:
    loading_label.config(text=f'Loading: [{i}%]')
    root.update_idletasks()
    time.sleep(0.1)
    i += 1

messagebox.showinfo(title='Alert', message='You have been hacked!')
root.destroy()

root.mainloop()
