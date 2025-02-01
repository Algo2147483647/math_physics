# Error Correction Code

[TOC]

## Problem

Error correction codes add redundant information to the original data at the sending end. This redundant information is related to the original data, and then the receiving end detects and corrects errors generated during the transmission process based on this correlation, thereby counteracting interference in the transmission process.

## Solution

### Linear Block Code

In linear codes, information bits and supervision bits are composed of some linear algebraic equations. The coding of grouping information codes and adding several supervision codes to each group of information codes is called block code. In block codes, supervision code elements only supervise the information code elements in this code group.

#### Hamming Code

Hamming code inserts $k$ bits of data as check bits into the original data, converting the original $n$ bits of data into $m$ ($m = n + k$) bits of code. Hamming code can only detect and correct one bit of error, and cannot detect errors of two or more bits.
$$
2^k - 1 \ge m \\
m = n + k
$$

#### Circular Code

In addition to the general properties of linear codes, cyclic codes also have cyclicity. Cyclicity means that any code group circulates one bit, that is, a code element at the right end is moved to the left end, or vice versa, and then it remains a code group in the code.

#### Low Density Parity Check (LDPC) Code

Low-density parity-check codes are constructed based on parity-check matrices with sparse matrix properties. For $(n, k)$ low-density parity-check codes, each $k$ bits of data is encoded using an $n$-bit codeword. The following is a parity-check matrix $H$ used by a $(16, 8)$ low-density parity-check code. It can be seen that the number of $1$ elements in the matrix is much less than the number of $0$ elements, so it has sparse matrix properties, which is the origin of low density.

### Convolutional Code

Convolutional code is a memory-based error correction code. The encoding rule is to encode $k$ information bits into $n$ bits. The encoded $n$ code elements are not only related to the current $k$ information input, but also to the previous $L-1$ groups of information.

#### Viterbi Decoding

Viterbi decoding is a dynamic programming algorithm.

### Turbo Code