# Compiler

[TOC]

## Formal Grammar

### Define  
Formal grammar is a 4-tuples
$$
G = <N, \Sigma, P>
$$

- $N$: **Nonterminal symbol**. It is replaced by groups of terminal symbols according to the production rules. $S \in N$: start symbol
- $\Sigma$: **Terminal symbol**. It is the elementary symbols of the language defined by a formal grammar.  And the terminals and non-terminals of a particular grammar are two disjoint sets.
- $P$: **Production rule**, each rule of the form as follows, where $*$ is the Kleene star operator and $\cup$ denotes set union. It is a rewrite rule specifying a symbol substitution that can be recursively performed to generate new symbol sequences.
  $$
  (\Sigma \cup N)^* N (\Sigma \cup N)^* \to (\Sigma \cup N)^*
  $$

### Include

- Context-free grammar (CFG)

- Context-sensitive grammar (CSG)

#### Context-free grammar (CFG)

**Define**
A context-free grammar (CFG) is a formal grammar whose production rules are of the form as follow, with $A$ a single nonterminal symbol, and $\alpha$ a string of terminals and/or non-terminals ($\alpha$ can be empty). A formal grammar is "context free" if its production rules can be applied regardless of the context of a nonterminal. 
$$
A \to \alpha
$$

**Include**

* Regular grammar: They require that all production rules have at most one non-terminal symbol, and that symbol is either always at the end or always at the start of the rule's right-hand side.

#### Context-sensitive grammar (CSG)

**Define**
A context-sensitive grammar is a formal grammar in which the left-hand sides and right-hand sides of any production rules may be surrounded by a context of terminal and nonterminal symbols.

## Lexical Analysis

### Tokens

### Finite Automaton

- Non-deterministic Finite Automaton
- Deterministic Finite Automaton

## Syntax Analysis, Parsing

### First Set & Follow Set

$$
f: N \to \{\Sigma\}
$$

**First Set**: FIRST(α)是α的所有可能推导的开头终结符或可能的ε. 计算方法:

- 在所要求的字符产生式的右边的第一位寻找终结符，假设该字符产生式集的第一位就是终结符，那么该终结符就是所要求的first集；
- 假设产生式的右边第一位是非终结符，那么继续寻找该非终结符的first集，直至寻找到一个终结符，即是起初所要求字符的first集；

**Follow Set**: FOLLOW(A)是所有该文法开始符推导的句型中出现在紧跟A之后的终结符或 “#”. 计算方法: 

- 在产生式的右边找到相应的字符，假设紧跟其后的是一个终结符，那么该终结符就是所要求的follow集
- 假设跟在其后的是一个非终结符，那么需要判断该非终结符是否可以为空：假如可以为空，那么将该产生式的左边的follow集加入到寻找集合当中，因为假如该非终结符为空的话，那么需要寻找产生这个非终结符的产生式左边的非终结符，因为产生式左边的非终结符的follow集就有可能是该非终结符的follow集；假如不为空，那么寻找该非终结符的first集，并将结果加入到搜索集合当中
- 直到不再有非终结符产生，找到所有的终结符，计算结束。

### up-bottom parser: $LL$ parsers

**Define**

up-bottom parser 是指从文法的开始符，从最抽象的起始非终结符 $S$ 向下推导出最具象的句子表达式。LL(1) parsers, 命名规则: 第一个L代表从左边开始扫描, 第二个L表示产生最左推导, 数字1表示每一步推导式只需要向后看一个符号就可以.  任何任意两个具有相同左部的产生式 $A \to \alpha | \beta$ 都满足:

- 如果α、β均不能推导出ε， $First(\alpha) \cap First(\beta) = \empty$
- α 和 β 至多有一个能推导出 ε.
- 如果 $β \Rightarrow ε$，则 FIRST(α) ∩ FOLLOW(A) = ∅

即, 没有公共左因子（如果有，那么无法只读一个字符就判断如何递归）, 不含有左递归（不包含回溯）
具体计算方法:

- 求出各个非终结符的first集和follow集
- 判断是不是LL(1)文法, 要求出select集, LL(1)判断方法：如果相同产生式左部的Select集有交集 $S’→S|ε : ε \in First(S’), and\ First(S’) \cap Follow(S’)≠\empty$, So the grammar is not LL(1)
- 构造分析表 $f(N, \Sigma)$

**Eliminate Left Recursion**

左递归可能导致递归下降解析器进入无限递归的情况，从而导致解析器无法正常工作。当一个非终结符的产生式中以它自己作为第一个符号出现时，就称为左递归。例如，对于产生式 A -> Aα，其中 A 是非终结符，α 是一个符号串，这就是左递归。
$$
\begin{align*}
A &\to A \alpha \\
&\to A A \alpha \\
&\to A A \cdots A \alpha \\
\end{align*}
$$
消除左递归，将左递归的产生式转换为等价的非左递归产生式。
$$
\begin{align*}
A &\to A \alpha | \beta\\
\Rightarrow A &\to \beta A'\\
A' &\to \alpha A' | \epsilon
\end{align*}
$$
**Removing Common Left Factoring** 

Common Left Factoring: 和数学中的公因子含义相同，就是公共的因子，而左公因子就是最左边的公因子。
$$
\begin{align*}
A &\to \alpha B_1 | \alpha B_2 | \cdots |\alpha B_n\\
\Rightarrow A &\to \alpha A'\\
A' &\to B_1 | \cdots | B_n
\end{align*}
$$

### bottom-up parser: $LR$ parsers

**Define**

bottom-up parser 是从最非终结符向上推导(规约), 最终规约得到起始非终结符 $S$. $LR(k)$ parsing is The most prevalent type of bottom-up parser today, where the “L” is for left-to-right scanning of the input, the“R” for constructing a rightmost derivation in reverse, and the $k$ for the number of input symbols of lookahead that are used in making parsing decisions. 

## Semantic Analysis

