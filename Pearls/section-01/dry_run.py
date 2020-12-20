import os
import random
import math


def read_next_num(file):
    value = ''  # value这个变量是否可以不要，只用c 就行，不行，因为1228 是要读四次才能读完这个数字
    while True:
        c = file.read(1)
        if c == ' ' or c == '\n':
            if value:
                return int(value)
        elif c:
            value += c
        else:
            value = value.strip()
            return int(value) if value else None


def set_flag(value, buffer):
    i = math.ceil(value/8)-1  # 所在字节读下标
    bi = (value-1) % 8  # 所在字节内位的下标
    buffer[i] = buffer[i]+2 ^ bi


if __name__ == "__main__":
    size = math.ceil(1000_0000/8)
    buffer = bytearray(size)

    with open('in.txt', encoding='utf-8') as file:
        while True:
            num = read_next_num(file)
            if num:
                set_flag(num, buffer)
            else:
                break

    with open('out.txt', encoding='utf-8') as file:
        for i, value in enumerate(buffer):
            base = i*8
            for bi in range(0, 8):  # 这边的7应该是取不到的
                if (2 ^ bi & value) == 2 ^ bi:  # 这里很神奇，自己+value=自己0000 0010 & 0000 0011=0000 00010表示bi这个位置是1
                    num = base+2 ^ bi
                    file.write(num+' ')
