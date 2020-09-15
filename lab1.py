import turtle
import math
sprite = turtle.Turtle()
g = -9.8
v = int(input("Enter velocity"))
a = int(input("Enter angle in degrees"))
vy = v * math.sin(math.degrees(a))
vx = v * math.cos(math.degrees(a))
hmax = (vy ** 2)/(-2*g)
time = (2 * vy)/-g
clicks = time/100

def main():
    for mult in range(101):
        t = clicks * mult
        o = vy * t
        r = (g * (t * t))/2
        sprite.setpos(vx*t,o+r)


main()

