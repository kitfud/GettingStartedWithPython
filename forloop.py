colors = ["red","green","blue","orange"]
# print(colors[0])

# for x in colors:
#     print(x)

# print(len(colors))

# for x in range(1,len(colors),2):
#      print(colors[x])

# def calculate(x):
#     return x+1
# print(calculate(3))

import time 
import tkinter 

root = tkinter.Tk()
myCanvas = tkinter.Canvas(root)

myCanvas.pack()

square = myCanvas.create_rectangle(0,0,100,100,fill="red")

#root.mainloop()
def colorChange():
    #for x in colors:
    for x in range(0,len(colors),2):
        myCanvas.itemconfig(square,fill=colors[x])
        root.update()
        time.sleep(1)


while True:
    colorChange()


