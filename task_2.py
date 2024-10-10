import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_rotate(t, order, size):
    ''' Поворачиваем черепашку 6 раз на 60 градусов, чтобы обойти круг '''
    for i in range(6):
        koch_curve(t, order, size)
        t.left(60)


def draw_koch_curve(order, size=150):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(-9)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_rotate(t, order, size)

    window.mainloop()

user_input = input ( "Введите уровень сложности фрактала (цифра): " )

# Виклик функції
draw_koch_curve(int(user_input))