import os
import time
import random
import math


def read_next_num(file):
    value = ''
    while True:
        c = file.read(1)  # 文件读取完毕后, 会返回''(一个字符也没有,长度为0)
        if c == ' ' or c == '\n':
            if value:
                return int(value)
        elif c:
            value += c
        else:
            # 这里是为了处理文件中最后一个数值直接结束文件, 没有额外的空格或换行
            return int(value) if value else None


def set_flag(value, buffer):
    i = math.ceil(value / 8)-1  # 计算所在字节的下标
    bi = (value-1) % 8  # 计算其所在字节内位的下标
    buffer[i] = buffer[i]+2 ** bi  # 设置flag


def big_size_numbers_sort():
    start = time.time()
    size = math.ceil(1000_0000 / 8)
    buffer = bytearray(size)

    with open('in.txt', encoding='utf-8') as file:
        while True:
            num = read_next_num(file)
            if num:  # 因为不可能返回0
                set_flag(num, buffer)
            else:
                break

    with open('out3.txt', 'w+', encoding='utf-8') as file:
        for i, value in enumerate(buffer):
            base = i*8
            for bi in range(1, 9):
                bit_value = 2**(bi-1)
                if value & bit_value != 0:
                    num = base + bi
                    file.write(str(num)+' ')
    interval = time.time()-start
    print(f'处理完毕, 共耗时: {interval:.2f}s')


if __name__ == "__main__":
    big_size_numbers_sort()

# 二进制和16进制的转换
# 类型: 如何看待二进制位
# 2个位运算 &(and运算, 与运输), |(或运算), ^
# 理解字节顺序相对偏移, 理解数值的相对相对偏移
# 0001 | 0000 0011  (Windows操作系统) 字节序
# 存整数, byte(8|1个字节), int(32|4字节, bigint,int合并了,所以不区分,无法确定int) (PyTorch-long(64|4字节))
# 字节顺, 高位字节在左边, 低位字节在右边(大端字节序 Bit-Little), 字节内部的位也可以认为是高位在左边你, 低位在右边(和我们日常使用的数值相反)
# 位标记: 只有1位是1, 其它位都是0, 因此对应的值就能等于: 2**n(n代表1所在下标(从0开始编号))
# 位标记: 在自己的进制内, 不可被分解为2个值相加, 为此可以用来检测其它值是否由位标记组合而成, 可以理解位分解
# 枚举类型都利用了: File 只读, 隐藏, 系统, 被锁定

# Unicode标准委员会
# utf-8: 英文1字节, 最常用的中文占2个字节, 部分占3个字节, 特殊中文占6个字节(兼容ASCII)
# utf-16: 2个字节, 或者4个字节(极少使用) (西方人极少使用)
# utf-32: 4个字节(谁都不喜欢)
# GB2312: 中国的标准 (兼容ASCII)
# BIG-5: 亚洲国家制定的编码(兼容ASCII)


# 0. 打开输入文件
# 1. 读取下一个数值(这个操作需要写成一个函数)
# 2. 判断数值是否为None, 如果是, 进入步骤4, 不是则进入步骤3
# 3. 将读入数值对于的序号在buffer中的位置设置为1(另外一个函数), 重写进入步骤1

# 4. 打开输出文件
