# Message Digest 5

[TOC]

## Define

[Hash_algorithm](./Hash_Algorithm.md)

Message-Digest Algorithm 5 (MD5) 可以产生出一个128位（16字节）的散列值（hash value），通常用一个32位的十六进制数表示。 MD5 散列是一种单向过程，设计上是不可逆的, 不能从MD5散列值逆向推导出原始数据。

## Process

### Padding

首先将原始数据按照规则填充，使其长度模512位的余数为448。填充始终发生，即使消息的长度已经等于448模512。填充的第一个位是`1`，之后都是`0`，直到满足长度条件。在填充的消息后面附加一个64位的长度字段，表示原始消息的长度（以位为单位）。这样，整个消息的长度就变成了512位的倍数。



### 循环计算

算法使用4个32位的寄存器（通常用A、B、C、D表示），它们被初始化为特定的值，这些值在MD5规范中定义。将消息分成512位的块（每块64字节）。每个块被进一步分解为16个32位的子块。MD5算法使用主循环，对每个64字节块进行一系列操作，每次操作都更新A、B、C、D四个寄存器。

MD5算法的核心是一个基于位操作的压缩函数，它包括四轮循环运算。每轮包含16个类似但不同的操作，每个操作基于一个非线性函数F、一个32位的子块、一个常数和一个左循环位移操作。在每一步中，一个子块和一个常数被加到其中一个寄存器中，然后通过特定的非线性函数处理，与另一个寄存器的内容合并，最后结果被旋转一个特定的数量，并加上第四个寄存器的内容。这样更新寄存器的内容。

## Implement

```python
# MD5算法
# 左循环移位函数
def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

# MD5中使用的辅助函数
def F(x, y, z):
    return (x & y) | (~x & z)

def G(x, y, z):
    return (x & z) | (y & ~z)

def H(x, y, z):
    return x ^ y ^ z

def I(x, y, z):
    return y ^ (x | ~z)

# 单个MD5转换
def md5_round(func, a, b, c, d, x, s, ac):
    a = (a + func(b, c, d) + x + ac) & 0xFFFFFFFF
    a = left_rotate(a, s)
    a = (b + a) & 0xFFFFFFFF
    return a

# T表，用于MD5转换的sin函数值的绝对值的整数部分
T = [int((2**32) * abs(math.sin(i + 1))) for i in range(64)]

# MD5主要算法
def md5_main(message):

    # 将输入消息转换为字节
    message = bytearray(message, 'utf-8')

    # 原始消息的位长度
    orig_len_in_bits = (8 * len(message)) & 0xffffffffffffffff

    # 填充
    message.append(0x80)
    while len(message) % 64 != 56:
        message.append(0)

    # 添加原始长度的低64位
    message += orig_len_in_bits.to_bytes(8, byteorder='little')

    # 初始化MD缓冲区（A, B, C, D）
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    # 主循环
    for i in range(0, len(message), 64):
        aa, bb, cc, dd = A, B, C, D
        chunk = message[i:i+64]
        for j in range(64):
            if 0 <= j <= 15:
                func = F
                g = j
            elif 16 <= j <= 31:
                func = G
                g = (5*j + 1) % 16
            elif 32 <= j <= 47:
                func = H
                g = (3*j + 5) % 16
            elif 48 <= j <= 63:
                func = I
                g = (7*j) % 16

            dTemp = D
            D = C
            C = B
            B = md5_round(func, A, B, C, D, int.from_bytes(chunk[4*g:4*g+4], byteorder='little'), S[j], T[j])
            A = dTemp

        # 更新MD缓冲区
        A = (A + aa) & 0xFFFFFFFF
        B = (B + bb) & 0xFFFFFFFF
        C = (C + cc) & 0xFFFFFFFF
        D = (D + dd) & 0xFFFFFFFF

    # 输出最终的MD5散列值
    return ''.join(map(lambda x: x.to_bytes(4, byteorder='little').hex(), [A, B, C, D]))

# 定义每一轮的左循环移位量
S = [
    # 第一轮
    7, 12, 17, 22] * 4 +
    # 第二轮
    [5, 9, 14, 20] * 4 +
    # 第三轮
    [4, 11, 16, 23] * 4 +
    # 第四轮
    [6, 10, 15, 21] * 4
]

# 使用MD5
test_string = "hello"
md5_hash = md5_main(test_string)
print(md5_hash)

```



## Problem

### 碰撞攻击

