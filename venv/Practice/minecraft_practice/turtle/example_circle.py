# Minecraft Turtle Example - Circle
import minecraft_turtle
from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

steve = minecraft_turtle.MinecraftTurtle(mc, pos)
steve.speed(10)

for step in range(0, 100):
    steve.right(5)
    steve.forward(2)