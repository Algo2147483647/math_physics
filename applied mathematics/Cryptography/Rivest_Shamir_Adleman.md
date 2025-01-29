# Rivest Shamir Adleman

[TOC]

## Define

Rivest Shamir Adleman (RSA) encryption is an [asymmetric encryption](./Asymmetric_Encryption.md) algorithm.

RSA算法的安全性基于质因数分解的难度：在公钥 $(n, e)$ 已知的情况下，如果没有私钥，对 $n$ 进行分解以找到 $p$ 和 $q$ 是非常困难的.

## Process

### Key generation
1. **选择两个大的质数** $p$ 和 $q$，且这两个数要足够大以使其乘积不容易被分解。
2. **计算这两个质数的乘积** $n = p \times q$。$n$ 的长度，即其以位（bit）为单位的数目，是密钥的长度。
3. **计算欧拉函数** $\phi(n)$（有时也记为 $\varphi(n)$，它等于 $(p-1) \times (q-1)$。
4. **选择一个整数** $e$，作为公开密钥的一部分，通常可以是65537，它满足 $1 < e < \phi(n)$ 并且 $e$ 和 $\phi(n)$ 互质。
5. **计算$e$的模逆元** $d$，满足 $e \times d \mod \phi(n) = 1$。这意味着 $d$ 是 $e$ 的模 $\phi(n)$ 的乘法逆元。

最终，公钥是 $(n, e)$，而私钥是 $(n, d)$。


### Encryption
提供公钥 $(n, e)$，将消息 $M$ 转换为一个整数 $m$，满足 $0 \le m < n$。然后计算加密后的消息 $c$ 使用公钥中的 $e$ 和 $n$：
$$
c = m^e \mod n
$$

### Decryption

使用私钥 $(n, d)$ 来解密
$$
m = c^d \mod n
$$
由于 $d$ 是 $e$ 的模 $\phi(n)$ 的逆，这将正确恢复消息 $M$。