"""
Minecraft Builder
가공된 blueprint 데이터를 읽어와
minecraft_turtle과 유사한 방법으로 block 건축
"""

from mcpi import minecraft
from mcpi import block
import time
import math


class MinecraftDrawing:
    def __init__(self, mc):
        self.mc = mc

    def drawPoint3d(self, x, y, z, blockType, blockData=0):
        self.mc.setBlock(x, y, z, blockType, blockData)

    # draws a face, when passed a collection of vertices which make up a polyhedron
    def drawFace(self, vertice, filled, blockType, blockData=0):
        edgesVertices = []
        firstVertex = vertice[0]
        lastVertex = vertices[0]

        # loop through vertices and get edges
        for vertex in vertice[1:]:
            # got 2 vertices, get the points for the edge
            edgesVertices = edgesVertices + self.getLine(
                lastVertex.x, lastVertex.y, lastVertex.z, vertex.x, vertex.y, vertex.z)
            # persist the last vertex found
            lastVertex = vertex

        # get edge between the last and first vertices
        edgesVertices = edgesVertices + self.getLine(
            lastVertex.x, lastVertex.y, lastVertex.z, vertex.x, vertex.y, vertex.z)

        if filled:
            # draw solid face
            # sort edges vertices
            def keyX(point):
                return point.x

            def keyY(point):
                return point.y

            def keyZ(point):
                return point.z

            edgesVertices.sort(key=keyZ)
            edgesVertices.sort(key=keyY)
            edgesVertices.sort(key=keyX)

            # draw lines between the points on the edges
            # this algorithm isnt very efficient, but it does always fill the gap
            lastVertex = edgesVertices[0]
            for vertex in edgesVertices[1:]:
                # got 2 vertices, draw lines between them
                self.drawLine(
                    lastVertex.x, lastVertex.y, lastVertex.z, vertex.x, vertex.y, vertex.z,
                    blockType, blockData)
                # persist the last vertex found
                lastVertex = vertex

        else:
            # draw wireframe
            slef.drawVertices(edgesVertices, blockType, blockData)

    # draw's all the points in a collection of vertices with a block
    def drawVertices(self, vertices, blockType, blockData):
        for vertex in vertices:
            self.drawPoint3d(vertex.x, vertex.y, vertex.z, blockType, blockData)

    def drawLine(self, x1, y1, z1, x2, y2, z2, blockType, blockData=0):
        self.drawVertices(self.getLine(x1, y1, z1, x2, y2, z2), blockType, blockData)

    def drawSphere(self, x1, y1, z1, radius, blockType, blockData=0):
        for x in range(radius * -1, radius):
            for y in range(radius * -1, radius):
                for z in range(radius * -1, radius):
                    if x ** 2 + y ** 2 + z ** 2 < radius ** 2:
                        self.drawPoint3d(x1 + x, y1 + y, z1 + z, blockType, blockData)

    def drawCircle(self, x0, y0, z, radius, blockType, blockData=0):
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        x = 0
        y = radius

        self.drawPoint3d(x0, y0 + radius, z, blockType, blockData)
        self.drawPoint3d(x0, y0 - radius, z, blockType, blockData)
        self.drawPoint3d(x0 + radius, y0, z, blockType, blockData)
        self.drawPoint3d(x0 - radius, y0, z, blockType, blockData)

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x

            self.drawPoint3d(x0 + x, y0 + y, z, blockType, blockData)
            self.drawPoint3d(x0 - x, y0 + y, z, blockType, blockData)
            self.drawPoint3d(x0 + x, y0 - y, z, blockType, blockData)
            self.drawPoint3d(x0 - x, y0 - y, z, blockType, blockData)

            self.drawPoint3d(x0 + y, y0 + x, z, blockType, blockData)
            self.drawPoint3d(x0 - y, y0 + x, z, blockType, blockData)
            self.drawPoint3d(x0 + y, y0 - x, z, blockType, blockData)
            self.drawPoint3d(x0 - y, y0 - x, z, blockType, blockData)

    def drawHorizontalCircle(self, x0, y, z0, radius, blockType, blockData=0):
        f = 1 - radius
        ddf_x = 1
        ddf_z = -2 * radius
        x = 0
        z = radius

        self.drawPoint3d(x0, y, z0 + radius, blockType, blockData)
        self.drawPoint3d(x0, y, z0 - radius, blockType, blockData)
        self.drawPoint3d(x0 + radius, y, z0, blockType, blockData)
        self.drawPoint3d(x0 - radius, y, z0, blockType, blockData)

        while x < z:
            if f >= 0:
                z -= 1
                ddf_z += 2
                f += ddf_z
            x += 1
            ddf_x += 2
            f += ddf_x

            self.drawPoint3d(x0 + x, y, z0 + z, blockType, blockData)
            self.drawPoint3d(x0 - x, y, z0 + z, blockType, blockData)
            self.drawPoint3d(x0 + x, y, z0 - z, blockType, blockData)
            self.drawPoint3d(x0 - x, y, z0 - z, blockType, blockData)

            self.drawPoint3d(x0 + z, y, z0 + x, blockType, blockData)
            self.drawPoint3d(x0 - z, y, z0 + x, blockType, blockData)
            self.drawPoint3d(x0 + z, y, z0 - x, blockType, blockData)
            self.drawPoint3d(x0 - z, y, z0 - x, blockType, blockData)

    # returns points on a line
    # 3d implementation of bresenham line algorithm
    def getLine(self, x1, y1, z1, x2, y2, z2):

        # return maximum of 2 values
        def MAX(a, b):
            if a > b:
                return a
            else:
                return b

        # return step
        def ZSGN(a):
            if a < 0:
                return -1
            elif a > 0:
                return 1
            elif a == 0:
                return 0

        # list for vertices
        vertices = []

        # if the 2 points are the same, return single vertice
        if x1 == x2 and y1 == y2 and z1 == z2:
            vertices.append(minecraft.Vec3(x1, y1, z1))

        # else get all points in edge
        else:

            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1

            ax = abs(dx) << 1
            ay = abs(dy) << 1
            az = abs(dz) << 1

            sx = ZSGN(dx)
            sy = ZSGN(dy)
            sz = ZSGN(dz)

            x = x1
            y = y1
            z = z1

            # x dominant
            if ax >= MAX(ay, az):
                yd = ay - (ax >> 1)
                zd = az - (ax >> 1)
                loop = True
                while loop:
                    vertices.append(minecraft.Vec3(x, y, z))
                    if x == x2:
                        loop = False
                    if yd >= 0:
                        y += sy
                        yd -= ax
                    if zd >= 0:
                        z += sz
                        zd -= ax
                    x += sx
                    yd += ay
                    zd += az

            # y dominant
            elif ay >= MAX(ax, az):
                xd = ax - (ay >> 1)
                zd = az - (ay >> 1)
                loop = True
                while loop:
                    vertices.append(minecraft.Vec3(x, y, z))
                    if y == y2:
                        loop = False
                    if xd >= 0:
                        x += sx
                        xd -= ay
                    if zd >= 0:
                        z += sz
                        zd -= ay
                    y += sy
                    xd += ax
                    zd += az

            # z dominant
            elif az >= MAX(ax, ay):
                xd = ax - (az >> 1)
                yd = ay - (az >> 1)
                loop = True
                while loop:
                    vertices.append(minecraft.Vec3(x, y, z))
                    if z == z2:
                        loop = False
                    if xd >= 0:
                        x += sx
                        xd -= az
                    if yd >= 0:
                        y += sy
                        yd -= az
                    z += sz
                    xd += ax
                    yd += ay

        return vertices

class MinecraftBuilder:
    SPEEDTIMES = {0: 0, 100:0.01, 10: 0.1, 9: 0.2, 8: 0.3, 7: 0.4, 6: 0.5, 5: 0.6, 4: 0.7, 3: 0.8, 2: 0.9, 1: 1}

    def __init__(self, mc, position=minecraft.Vec3(0, 0, 0), blueprint=""):
        # set defaults
        self.mc = mc
        # set start position
        self.startposition = minecraft.Vec3(0,0,0)
        self.startposition.x = int(position.x)
        self.startposition.y = int(position.y)
        self.startposition.z = int(position.z)
        # set builder position
        self.position = position
        # set blueprint
        self.blueprint = blueprint

        # set speed
        self.builderspeed = 10
        # show builder
        self.showbuilder = True
        # create drawing object
        self.mcDrawing = MinecraftDrawing(self.mc)
        # set builder block
        self.builderblock = block.Block(block.DIRT.id)

    def set_position(self, x, y, z):
        # clear the builder
        # if self.showbuilder:
        #     self._clearBuilder(self.position.x, self.position.y, self.position.z)

        # update the position
        # self.position = self.startposition + minecraft.Vec3(x,y,z)
        self.position.x = self.startposition.x + x
        self.position.y = self.startposition.y + y
        self.position.z = self.startposition.z + z
        # print(self.position)

        # wait
        time.sleep(self.SPEEDTIMES[self.builderspeed])

        # draw the builder
        if self.showbuilder:
            self._drawBuilder(self.position.x, self.position.y, self.position.z)

    def set_speed(self, builderspeed):
        self.builderspeed = builderspeed

    def set_blueprint(self, blueprint):
        self.blueprint = blueprint

    def build(self):
        # 읽을 수 없으면 build 취소
        if not self._readBlueprint():
            return

        for data in self.blueprint_data:
            # print(data)
            self.set_position(data['x'], data['y'], data['z'])

    def _readBlueprint(self):
        f = open(self.blueprint, 'r')
        self.blueprint_data = []

        try:
            result = True
            datas = f.readlines()

            for data in datas:
                x, z, y, block = data.split('\t')
                # print(f"{x} {y} {z} {block}")
                self.blueprint_data.append(
                    {"x": int(x), "y": int(y), "z": int(z), "block": block})

        except FileNotFoundError as e:
            print(e)
            result = False
        finally:
            f.close()

        return result

    def _drawBuilder(self, x, y, z):
        # draw builder
        self.mcDrawing.drawPoint3d(x, y, z, self.builderblock.id, self.builderblock.data)

    def _clearBuilder(self, x, y, z):
        # clear builder
        self.mcDrawing.drawPoint3d(x, y, z, block.AIR.id)


if __name__=="__main__":
    mc = minecraft.Minecraft.create()
    pos = mc.player.getPos()

    builder = MinecraftBuilder(mc, pos)

    # builder.set_blueprint("deposit-rail-crane.txt")
    # builder.set_blueprint("Deposit Rail Crane.txt")
    # builder.set_blueprint("tiny-house.txt")
    # builder.set_blueprint("Tiny House.txt")

    builder.set_blueprint("plantation-mansion.txt")
    builder.set_speed(100)

    builder.build()
