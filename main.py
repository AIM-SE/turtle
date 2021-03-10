import turtle

turtle.speed(0)
turtle.ht()

size = 30

for y in range(8):
  for x in range(8):
    turtle.up()
    turtle.goto(x*size, y*size)
    turtle.down()

    if y % 2 == x % 2:
      turtle.color("dark goldenrod")
    else:
      turtle.color("wheat")

    turtle.begin_fill()
    for _ in range(4):
      turtle.forward(size)
      turtle.left(90)
    turtle.end_fill()



  