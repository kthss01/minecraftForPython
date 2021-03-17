# Minecraft Turtle Example - Spiral
import minecraft_turtle
from mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

steve = minecraft_turtle.MinecraftTurtle(mc, pos)

steve.penblock(block.TNT.id, 1)
steve.speed(10)
steve.up(5)

for step in range(0, 100):
    steve.forward(2)
    steve.right(10)