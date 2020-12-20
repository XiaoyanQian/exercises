import os
import time
import random


def write_list_to_file(values, path):
    # 序列化-->自定义格式的文本序列化
    with open(path, 'a+', encoding='utf-8') as file:
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


def big_size_numbers_sort():
    start = time.time()

    for i in range(0, 100):
        start = i*10_0000+1
        end = (i+1)*10_0000
        values = []

        with open('in.txt', encoding='utf-8') as file:
            while True:
                value = read_next_num(file)
                if value:  # 是当前范围内的值
                    if value >= start and value <= end:
                        values.append(value)
                else:
                    break;

        if values:
            values.sort()
            write_list_to_file(values, 'out2.txt')

    interval = time.time()-start
    print(f'处理完毕, 共耗时: {interval:.2f}s')


if __name__ == "__main__":
    big_size_numbers_sort()
