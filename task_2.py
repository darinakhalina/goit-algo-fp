import turtle


def pythagorean_tree(t, order, size, angle=45):
    if order == 0:
        return
    else:
        t.forward(size)
        t.left(angle)
        pythagorean_tree(t, order - 1, size * 0.7, angle)
        t.right(2 * angle)
        pythagorean_tree(t, order - 1, size * 0.7, angle)
        t.left(angle)
        t.backward(size)


def draw_pythagorean_tree(order, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(0, 0)
    t.left(90)
    t.pendown()
    t.color("green")

    pythagorean_tree(t, order, size)

    window.mainloop()


def main():
    try:
        recursion_level = int(input("Введіть рівень рекурсії: "))
        draw_pythagorean_tree(recursion_level)
    except ValueError:
        print("Будь ласка, введіть число.")


if __name__ == "__main__":
    main()
