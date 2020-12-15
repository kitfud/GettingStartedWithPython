import turtle 

t = turtle.Pen()
t.color("red")
# t.forward(100)
# t.left(90)

def square(s):
    for x in range(4):
        t.forward(int(s))
        t.left(90)

def triange(s):
    t.forward(s)
    for x in range(2):
        t.left(120)
        t.forward(s)

# triange()
# square()
# square()
while True:
    choice = input("square enter s, triange enter t")
    size = input("give me a size of a shape SIZE")
    if choice == "s":
        square(size)
    elif choice == "t":
        triange(int(size))
turtle.done()