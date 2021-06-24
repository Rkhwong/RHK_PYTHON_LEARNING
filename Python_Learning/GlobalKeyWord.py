

c = 1 # global Variable

def add ():
    global c # You can change a Global Variable defining it
    c = c + 2
    print(c)

add()