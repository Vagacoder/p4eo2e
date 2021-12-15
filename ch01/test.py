from ezgraphics import GraphicsWindow

print("Hello world")

win = GraphicsWindow(400, 200)
canvas = win.canvas()

canvas.setColor("red")
canvas.drawRect(10, 20, 100, 20)


win.wait()
