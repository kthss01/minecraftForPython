# Minecraft Turtle Example
import minecraft_turtle
from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

steve = minecraft_turtle.MinecraftTurtle(mc, pos)

steve.speed(10)

# draw a square
steve.forward(10)
steve.right(90)
steve.forward(10)
steve.right(90)
steve.forward(10)
steve.right(90)
steve.forward(10)

# draw a square on the floor
steve.walk()
steve.forward(11)
steve.right(90)
steve.forward(10)
steve.right(90)
steve.forward(10)
steve.right(90)
steve.forward(10)
