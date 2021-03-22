# Minecraft Turtle Example
import minecraft_turtle
from mcpi import minecraft


def f(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        f(turtle, length / 3, depth - 1)
        turtle.right(60)
        f(turtle, length / 3, depth - 1)
        turtle.left(120)
        f(turtle, length / 3, depth - 1)
        turtle.right(60)
        f(turtle, length / 3, depth - 1)


mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

steve = minecraft_turtle.MinecraftTurtle(mc, pos)

steve.speed(0)

f(steve, 500, 6)
