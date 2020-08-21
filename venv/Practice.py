# 현재 위치 찾기
from mcpi import minecraft

mc = minecraft.Minecraft.create()

pos = mc.player.getPos()
print(pos)

# 순간이동 (Teleport, 텔레포트)
# x, y, z = mc.player.getPos()
# mc.player.setPos(x, y + 100, z)

# 블록 (block) 설치
# x, y, z = mc.player.getPos()
# mc.setBlock(x + 1, y, z, 1)

# 특수 블록
# 양모(wool) 같은 경우에는 색깔을 추가로 설정해야 함
# wool = 35
# mc.setBlock(x, y, z + 1, wool, 1)

# 다수 블록 설치
# stone = 1
# x, y, z = mc.player.getPos()
# mc.setBlocks(x + 1, y + 1, z + 1, x + 11, y + 11, z + 11, stone)

# 걸어가면서 블록설치하며 지나가기
# from time import sleep
#
# flower = 38
#
# while True:
#     x, y, z = mc.player.getPos()
#     mc.setBlock(x, y, z, flower)
#     sleep(0.1)

# 잔디 위에만 꽃을 심고 싶을 때
# x,y,z = mc.player.getPos() # 플레이어 위치
# block_beneth = mc.getBlock(x,y-1,z) # 블록 id
# print(block_beneth)

# from time import sleep
#
# grass = 2
# flower = 38
#
# while True:
#     x, y, z = mc.player.getPos()
#     block_beneth = mc.getBlock(x, y - 1, z)
#
#     if block_beneth == grass:
#         mc.setBlock(x, y, z, flower)
#     else:
#         mc.setBlock(x, y - 1, z, grass)
#
#     sleep(0.1)

# 폭탄 블록 가지고 놀기
# x, y, z = mc.player.getPos()
# tnt = 46
# # mc.setBlock(x, y, z, tnt)
# # mc.setBlock(x, y, z, tnt, 1) # data 넣어줘야 터짐 파괴 범위 같음
# mc.setBlocks(x + 1, y + 1, z + 1, x + 11, y + 11, z + 11, tnt, 1)

# 흐르는 용암 가지고 ㅗㄹ기
x, y, z = mc.player.getPos()
lava = 10
mc.setBlock(x + 3, y + 3, z, lava) # 이 블록에서 용암이 흐르기 시작함
# 용암은 식으면 돌이 됨
