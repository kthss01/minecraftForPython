# Minecraft Turtle Example

import minecraft_turtle
from mcpi import minecraft
from mcpi import block


def tree(branchLen, t):
    if branchLen > 6:
        if branchLen > 10:
            t.penblock(block.WOOD)
        else:
            t.penblock(block.LEAVES)

    # for performance
    x, y, z = t.position.x, t.position.y, t.position.z
    # draw branch
    t.forward(branchLen)

    t.up(20)
    tree(branchLen - 2, t)

    t.right(90)
    tree(branchLen - 2, t)

    t.left(180)
    tree(branchLen - 2, t)

    t.down(40)
    t.right(90)
    tree(branchLen - 2, t)

    t.up(20)

    # go back
    t.setposition(x, y, z)

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()

steve = minecraft_turtle.MinecraftTurtle(mc, pos)

# point up
steve.setverticalheadings(90)

# set speed
steve.speed(0)

# call the tree fractal
tree(20, steve)
