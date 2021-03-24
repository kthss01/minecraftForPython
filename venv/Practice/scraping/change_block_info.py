# block info id와 data 가공

# id 가공
def make_info_id(path='./block_info_id.txt'):
    blocks = {}

    with open(path, 'r') as f:
        # data = f.readlines()
        # print(data)
        datas = f.readlines()

        for data_str in datas:
            # print(data)
            data_list = data_str.split()
            block_name = data_list[0]
            block_id = int(data_list[2][6:-1])
            # print(f"{block_name} {block_id}\n")
            blocks[block_name] = block_id

    # print(blocks)

    with open('blocks_id.txt', 'w') as f:
        for name, id in blocks.items():
            f.write("{}\t{}\n".format(name, id))


# data 가공
def make_info_data(path='./block_info_data.txt'):
    blocks = {}

    with open(path, 'r') as f:
        datas = f.readlines()
        # print(datas)

        temp_blocks = []

        for data_str in datas:
            if data_str == "\n":
                # print(temp_block)
                block_name = temp_blocks[0][:-2]
                blocks[block_name] = []

                for block in temp_blocks:
                    if block[:-2] == block_name:
                        continue

                    block_list = block.split()
                    block_data_id = block_list[0][:-1]
                    # print(block_list[1:])
                    block_data_name = " ".join(block_list[1:])

                    blocks[block_name].append({'id':block_data_id, 'name':block_data_name})

                temp_blocks.clear()
                continue

            temp_blocks.append(data_str)

        block_name = temp_blocks[0][:-2]
        blocks[block_name] = []

        for block in temp_blocks:
            if block[:-2] == block_name:
                continue

            block_list = block.split()
            block_data_id = block_list[0][:-1]
            # print(block_list[1:])
            block_data_name = " ".join(block_list[1:])

            blocks[block_name].append({'id': block_data_id, 'name': block_data_name})

    # print(blocks)

    with open('blocks_data.txt', 'w') as f:
        for block_name in blocks.keys():
            # print(block_name)

            for block in blocks[block_name]:
                # print(block)
                # print(block_data_id + "_" + block_data_name)
                f.write("{}\t{}\t{}\n".format(
                    block_name,
                    block['name'],
                    block['id']))


if __name__ == '__main__':
    make_info_id()

    make_info_data()
