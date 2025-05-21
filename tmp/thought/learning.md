# Learning

[TOC]

### 思考 + 实践

实践是检验真理的唯一标准.

---

学而不思则惘, 思而不学则怠.

---

人的思维成长，是一个交织着长期积累 (量变)与瞬间顿悟 (质变)的过程。

当实践经验积累到临界点 (实践)，意识便会发现 事物间的内在关联从迷雾中逐渐显现 (思考)。主动将原本孤立的素材从点集连接成网络，构建一个完整且自洽的知识系统，从而实现认知质变。

因此，实践不够素材不足，事物间的关联无从体现，再空想也是怠惰 (怠)。事情做了素材有了，但是不及时整理复盘，记忆会逐渐遗忘，再刻苦努力也只是惘然 (惘)。

---

数学，惟自己推算一遍，
算法，惟自己实现一遍，
知识，惟自己讲解一遍。

自己整一遍，瞬间就明白，明白了就记住了。不去做，就一直云里雾里，也记不住。

---

不是什么课都可以通过看书看明白了，又不是理论物理和数学。工程性的实践学科, 只有亲手摆弄实验和模型，才能整明白。

---

In mathematics you don't understand things. You just get used to them.  (von Neumann)

---

AI 作为工具存在一个深刻的隐患, 人容易产生一种错觉，认为自己能够轻松解决问题，并将 AI 提供的浅显结果视为最终答案。这种依赖导致思想的惰性，使人丧失本该长期积累和自我训练才能获得的深度思考能力。事实上，AI 提供的只是一个大纲和即时的思维指引，修行始终在于个人。

### 解构 + 建构

认知思维分为两个方向:

解构抽象: 从复杂现象中抽象出普遍规律和基本原理。典型代表是数理，如从小学代数抽象出更普适的群论，从电磁现象抽象出 Maxwell 方程组。核心是归纳-演绎和Occam's 剃刀原理剥离表象干扰。

建构系统: 将简单的要素通过结构化设计构建出完整自洽的复杂系统。典型代表是工程技术，如用千万行代码构建出庞杂的企业营销平台, 用万亿级与或非门构建出精密的现代计算机。核心是在不断实践、积累经验中总结的设计模式，将复杂性约束在人脑企及的范围内。

两种思维协同演进, 解构思维为系统建构提供基础单元与原理支撑，建构思维推动数理公理化体系的逻辑完整自洽。

---

如非必要, 勿增实体.

Non sunt multiplicanda entia sine necessitate.

The simplest explanation is usually the correct one.

(Occam's razor)

---

复杂性不会消失, 只会转移.

---

### 表相 + 本质

透过表相看本质

当事物本身孤立来看，不能很好定义时 —— 可以通过与这个事物相互关联的外部，实现对该事物本身的定义。

---

数学中, 矢量、张量、函数本身是独立存在的数学实体 [本质]。—— 只是进行分析计算时, 需借助和指定基向量和坐标, 将其表现为数列、数阵、n元参数化函数的形式 [表相], 而这个形式会随着坐标选择的改变而变。

因此, 需要分清本质和表象的区别, 这些数列、数阵、箭头并非是矢量的本质, 其真正本质是只要能满足线性空间以下公理的集合都是矢量. 

Additive Closure: x+y \in V
Scalar Multiplication Closure: k x \in V
Identity element of vector addition: x+0=x
Inverse elements of vector addition: x+(-x) = 0
Identity element of scalar multiplication: 1x = x
Commutativity of vector addition: x+y = y+x
Associativity of vector addition: x+(y+z) = (x+y) +z
Compatibility of scalar multiplication with field multiplication: a(bx) = (a b)x
Distributivity of scalar multiplication with respect to vector addition: a(x+y) = a x + a y
Distributivity of scalar multiplication with respect to field addition: (a+b)x = ax+bx

Golang 里面的 interface 和线性空间的数学定义很像 —— 如何定义一个抽象? 定义他的行为。只要他的行为符合我们预期的标准, 那么他就属于我们定义的抽象

## 工程

工程的核心是解决方案：背景 - 问题 - 解法. 系统是对一个宏大工程问题的综合性解决方案。因此，系统是和环境(问题集合)长期磨合后的产物。也同样随着环境的变化而动态演变。一个优秀的系统，一定是因地制宜的，并以所处的环境为基础，正向循环演化能够解决更多的问题，适应更广的环境。