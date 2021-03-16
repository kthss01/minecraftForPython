'''
마인크래프트 청사진 (blueprint)

1. 수작업 전 기초 blueprint 만들기
    간단하게 width height depth와 가장 많은 block을 입력 받아
    기초 blueprint 작성

2. 수작업 후 blueprint 체크하기
    작성한 blueprint 읽어와 block 갯수를 비교
    block들 종류별 나열

3. 수작업 중 발생했던 blueprint 수정
    , -> \t로 변경
'''


# 기초 blueprint 만들기
def make_blueprint(filename, width, height, depth, basicBlock):
    with open(f'blueprints/{filename}.txt', 'w') as f:
        for h in range(height):
            for w in range(width):
                for d in range(depth):
                    f.write(f'{w}\t{d}\t{h}\t{basicBlock}\n')


# blueprint 체크
def check_blueprint(filename, width, height, depth, blockCount):
    with open(f'./blueprints/{filename}.txt', 'r') as f:
        blocksData = f.readlines()
        count = len(blocksData)
        print('realBlockCount = {0}, blockCount = {1}'.format(blockCount, count))

        blockDetailMaterials = {}

        for blockData in blocksData:
            # blockDataList = blockData.strip().split('\t')
            # print(blockDataList)
            w, h, d, block = blockData.strip().split('\t')
            # print(block)

            if block not in blockDetailMaterials:
                blockDetailMaterials[block] = 1
            else:
                blockDetailMaterials[block] += 1



        for key, value in sorted(blockDetailMaterials.items(),
                                 reverse=True, key=lambda x : x[1]):
            print(f"{key} = {value}")

# 수작업 중 발생했떤 blueprint 수정
# , -> \t로 변경
# def change_blueprint(filename):
#     blockData = []
#
#     with open(f'./blueprints/{filename}.txt', 'r') as f:
#         blocksData = f.readlines()
#
#     # for blockData in blocksData:
#     #     print(blockData.replace(',' , '\t'))
#
#     with open(f'./blueprints/{filename}.txt', 'w') as f:
#         for blockData in blocksData:
#             f.write(blockData.replace(',', '\t'))


if __name__ == '__main__':
    filename = 'Tiny House'
    width = 7
    height = 7
    depth = 11
    basicBlock = 'Grass'
    blockCount = 201

    # filename = 'Deposit Rail Crane'
    # width = 10
    # height = 5
    # depth = 5
    # basicBlock = 'Oak Wood Stairs'
    # blockCount = 68

    # make_blueprint(filename, width, height, depth, basicBlock)

    # change_blueprint(filename)
    check_blueprint(filename, width, height, depth, blockCount)

