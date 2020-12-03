import tkinter

root = tkinter.Tk()
myCanvas = tkinter.Canvas(root)
myCanvas.pack()

colors = ["red","green","blue","orange"]
myCanvas.create_rectangle(0,0,100,100,fill = colors[3])
root.mainloop()
# colors.append("white")
# colors.append("orange")

# colors.pop()
# colors.pop()

# colors[1] = "purple"

# colors.insert(2,"teal")

# colors.remove("green")
# del colors[2]
# print(colors)