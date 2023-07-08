import pgzrun
import math


list1 = []
list2 = []
list3 = []

WIDTH = 800
HEIGHT = WIDTH

clock = 0
realtime = 0
speed = 100
credits = 0
st_capital = 100
coeff_raise = 1.2 * (100//speed)
coef_prop = WIDTH / 400

p1 = 100
p2 = 50

det = 32
dev = WIDTH//det

cells = det**2

BLUE = 0, 128, 255
SAND1 = 255, 255, 120
SAND2 = 255, 255, 180
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 255, 0


def attack(n):

    global list1
    global list2
    global list3

    if p1 > p2:
        for j in range(len(list2)):
            if list2[j] != n:
                list3.append(list2[j])

        list2 = list3.copy()
        list3 = []
        list1.append(n)


def update():
    global clock
    global realtime
    global credits, coeff_raise, st_capital
    print(clock)
    clock += 10
    if clock > speed:
        realtime = clock // speed
    credits = st_capital + realtime*coeff_raise


def start():
    for i in range(det**2):
        if i == det-1:
            print('lol')
        else:
            x1 = dev * ((i + det) % det)
            y1 = dev * (i // det)
            x2 = x1 + dev
            y2 = y1 + dev

            if i in list1:
                BOX = Rect(x1, y1, x2, y2)

                screen.draw.filled_rect(BOX, SAND1)

            elif i in list2:
                BOX = Rect(x1, y1, x2, y2)

                screen.draw.filled_rect(BOX, SAND2)

            else:

                BOX = Rect(x1, y1, x2, y2)
                screen.draw.filled_rect(BOX, BLUE)


def draw():
    start()
    text()


def text():
    global credits, realtime

    print(credits)
    BOX = Rect(0, 0, (75 + 8 * math.log(credits,10))*coef_prop, 40*coef_prop)
    screen.draw.filled_rect(BOX, BLACK)
    screen.draw.text(f'Credits: {round(credits)}',
                     fontsize=20*coef_prop,
                     pos=(5*coef_prop, 20*coef_prop),
                     color=WHITE,
                    )
    screen.draw.text(f'Time: {realtime}',
                     fontsize=20*coef_prop,
                     pos=(5*coef_prop, 5*coef_prop),
                     color=WHITE,
                     )


def on_mouse_down(pos, button):

    global speed

    if button == mouse.LEFT:
        number = (pos[0]//dev) + (pos[1]//dev)*det

        print(number)
        x1 = dev * (((number + det) % det))
        y1 = dev * ((number // det))
        x2 = x1 + dev
        y2 = y1 + dev
        BOX = Rect(x1, y1, x2, y2)
        RED = 215, 123, 0

        if number == det - 1:
            speed = 50
            print('speed')
            screen.draw.filled_rect(BOX, RED)
            print(BOX)
        else:
            attack(number)
            screen.draw.filled_rect(BOX, SAND1)


pgzrun.go()
