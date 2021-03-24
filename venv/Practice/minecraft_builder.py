"""
Minecraft Builder
가공된 blueprint 데이터를 읽어와
minecraft_turtle과 유사한 방법으로 block 건축
"""

from mcpi import minecraft
from mcpi import block
import time
import math


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

    def set_block(self, x, y, z, block_id = block.DIRT.id, block_data=0):

        # update the position
        # self.position = self.startposition + minecraft.Vec3(x,y,z)
        self.position.x = self.startposition.x + x
        self.position.y = self.startposition.y + y
        self.position.z = self.startposition.z + z
        # print(self.position)

        # wait
        time.sleep(self.SPEEDTIMES[self.builderspeed])

        self._drawBuilder(self.position.x, self.position.y, self.position.z, block_id, block_data)

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
            self.set_block(data['x'], data['y'], data['z'])

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

    def _drawBuilder(self, x, y, z, block_id, block_data):
        # draw builder
        self.mc.setBlock(x, y, z, block_id, block_data)


if __name__=="__main__":
    mc = minecraft.Minecraft.create()
    pos = mc.player.getPos() + minecraft.Vec3(1, 1, 1)

    builder = MinecraftBuilder(mc, pos)

    # 예제 blueprint
    # filename = "tiny-house.txt"
    filename = "deposit-rail-crane.txt"
    # filename = "Deposit Rail Crane.txt"
    # filename = "Tiny House.txt"

    # 대형 blueprint test
    # filename = "plantation-mansion.txt"
    # builder.set_speed(100)

    path = "./scraping/blueprints/"
    blueprint = path + filename

    builder.set_blueprint(blueprint)

    builder.build()
