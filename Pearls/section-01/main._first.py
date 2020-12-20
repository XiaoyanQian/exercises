import os
import time
import random

# 生成随机数


def create_nums():
    values = set()
    for _ in range(0, 300_0000):
        value = random.randint(1, 1000_0000)
        if value not in values:
            values.add(value)

    with open('in.txt', 'w+', encoding='utf-8') as file:
        for value in values:
            file.write(str(value)+' ')


def write_list_to_file(values, path):
    # 序列化-->自定义格式的文本序列化
    with open(path, 'w+', encoding='utf-8') as file:
        for value in values:
            file.write(str(value)+' ')


def read_next_num(file):
    value = ''
    while True:
        c = file.read(1)
        if c == ' ' or c == '\n':
            if value:
                return int(value)
        elif c:
            value += c
        else:  # 读取到了文件结尾
            value = value.strip()
            return int(value) if value else None


def read_next_batch(file, size=5):
    values = []
    while True:
        value = read_next_num(file)
        if value != None:
            values.append(value)
            if len(values) == size:
                return values
        else:
            return values


# 第一种解决方案: 归并排序
def hander_batch(values):
    values.sort()

    new_path = 'new.txt'
    old_path = 'out.txt'
    current_path = 'current.txt'

    write_list_to_file(values, current_path)
    with open(current_path, 'r', encoding='utf-8') as current_file:
        with open(old_path, 'r', encoding='utf-8') as old_file:
            with open(new_path, 'w+', encoding='utf-8') as new_file:
                old_value = read_next_num(old_file)
                current_value = read_next_num(current_file)

                while True:
                    if old_value != None and current_value != None:
                        if current_value < old_value:
                            new_file.write(str(current_value)+' ')
                            current_value = read_next_num(current_file)
                        else:
                            new_file.write(str(old_value)+' ')
                            old_value = read_next_num(old_file)
                    elif old_value != None:
                        new_file.write(str(old_value)+' ')
                        old_value = read_next_num(old_file)
                    elif current_value != None:
                        new_file.write(str(current_value)+' ')
                        current_value = read_next_num(current_file)
                    else:
                        break

    os.remove(current_path)
    os.remove(old_path)
    os.rename(new_path, old_path)


def big_size_numbers_sort():
    start = time.time()
    with open('in.txt', encoding='utf-8') as file:
        while True:
            batch = read_next_batch(file, 10_0000)
            if batch:
                hander_batch(batch)
            else:
                break
    interval = time.time()-start
    print(f'处理完毕, 共耗时: {interval:.2f}s')


if __name__ == "__main__":
    #big_size_numbers_sort()
    create_nums()
    
