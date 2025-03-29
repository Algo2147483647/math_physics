# Abstract Syntax Tree

[TOC]

## Define

An **abstract syntax tree** is a [rooted tree](../../math/tree.md) representation of the abstract syntactic structure in a formal language.

- Value nodes: The leaf nodes of the abstract syntax tree are value nodes such as constants and variables.

$$
\{const, var\}
$$

- Function nodes: The non-leaf nodes are the function nodes such as functions. Meanwhile the children nodes  of a operation node are all parameters of this function, and its purpose is to map child nodes and itself to a value node.

$$
f(x_1, x_2, \cdots , x_n)
$$

## Function nodes

### Basic operators

- Logical operations
  - logical and
  - logical or
  - logical not
- Bitwise operations
  - bitwise and
  - bitwise or
  - bitwise not
  - bitwise xor
  - left shift
  - right shift
- Basic algebraic operators
  - addition
  - negative
  - multiplication
  - division
  - modulo (remainder)
  - exponent
  - root
- Comparison operators
  - greater than
  - greater than or equal to
  - equal to
  - less than
  - less than or equal to
  - between (open, close, left open, right open)
- Set operators
  - in
  - subset
  - number
  - ordered set operators
    - min / max
    - argmin / argmax
    - sort
  - number set operators
    - sum
- Memory operators
  - get address
  - dereference (access the value pointed to by the pointer)
  - assignment

### Logical

- Conditional Branches
- Loop

### Function

Function processing process: 

- Before processing
- Execution
- After processing

## Value nodes

### Constants + Variables

### Primary Value

- Null / Any
- Integer: int 8bit (char), int 16bit, int 32bit, int 64bit
- Floating-point number: float 32bit, float 64bit
- Boolean: true / false
- Pointer

### Data Structure

- Set
- Map
- Array (Vector)
  - String
- Matrix
- Structure (Tuple)
- Deque
- Function