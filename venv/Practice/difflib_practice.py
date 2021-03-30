"""
파이썬 두 문자열 비교하기 difflib
"""

from difflib import SequenceMatcher
from difflib import get_close_matches

def read_block_info():
    block_info = []

    with open('./scraping/blocks_id.txt', 'r') as f:

        for line in f.readlines():
            block_info.append(line.split('\t')[0])

    return block_info

def read_blocks():
    blocks = []

    with open('./scraping/blueprints/tiny-house.txt', 'r') as f:

        for line in f.readlines():
            blocks.append(line.split('\t')[-1].strip())

    return blocks

def find_similar_block(block, block_info):
    block_upper = block.upper()

    cutoff = 0.3  # 정확도

    result = get_close_matches(block_upper, block_info, cutoff=cutoff)

    if not result:  # 빈 리스트인 경우 false
        print("\t\t\t{} not found ".format(block))
        return 'AIR'  # 대체 블락 우선은 DIRT로 설정
    else:
        return result[0]  # 가장 정답에 가까운 값 반환

def test():
    """테스트"""
    block = "Mossy Stone Bricks"
    info = "STONE_BRICK"
    info2 = "MOSS_STONE"  # 비교군
    info3 = "STONE"  # 비교군

    # 참고 : 0.6 정도는 나와야 일치한다고 본다고 함

    print(SequenceMatcher(None, block, info).ratio())  # 0.13

    block2 = block.upper()

    print(SequenceMatcher(None, block2, info).ratio())  # 0.68

    print(SequenceMatcher(None, block2, info2).ratio())  # 0.64

    print(SequenceMatcher(None, block2, info3).ratio())  # 0.43

def basic_practice():
    """기본 예제"""
    str1 = 'abc'
    str2 = 'abc'

    ratio = SequenceMatcher(None, str1, str2).ratio()
    print(ratio)

    str1 = 'abcd'
    str2 = 'dabc'

    ratio = SequenceMatcher(None, str1, str2).ratio()
    print(ratio)

    str1 = 'abcd'
    str2 = 'efgh'

    ratio = SequenceMatcher(None, str1, str2).ratio()
    print(ratio)

    word = 'appel'
    # word = 'orange'

    word_list = ['ape', 'apple', 'peach', 'puppy']

    result = get_close_matches(word, word_list)

    print(result)


if __name__ == '__main__':
    # basic_practice()

    # test()

    # print(read_block_info())
    block_info = read_block_info()

    # print(read_blocks())
    blocks = read_blocks()

    not_find_cnt = 0

    for block in blocks:
        result = find_similar_block(block, block_info)

        # 못찾은 거
        if result == 'AIR':
            not_find_cnt += 1

        print(result)

    print(not_find_cnt)