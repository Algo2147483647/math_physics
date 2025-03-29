# Abstract Syntax Tree

[TOC]

## Define

An **abstract syntax tree** is a [rooted tree](../../math/tree.md) representation of the abstract syntactic structure in a formal language.

- Value nodes: The leaf nodes of the abstract syntax tree are value nodes such as constants and variables.

$$
\{const, var\}
$$

- operation nodes: The non-leaf nodes are the operation nodes such as functions. Meanwhile the children nodes  of a operation node are all parameters of this function.

$$
f(x_1, x_2, \cdots , x_n)
$$



## Operations

### Basic operators

- Logical operations
  - logical and
  - logical or
  - logical not
- Bitwise operations
  - bitwise and
  - bitwise or
  - bitwise negation (unary operator)
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
- Memory operators
  - get address
  - dereference (access the value pointed to by the pointer)
- Assignment operator

### Logical

- Loop
- Conditional Branch

### Function

## Value

### Constants + Variables

### Primary Value

- Integer
  - int 8bit (char)
  - int 16bit
  - int 32bit
  - int 64bit
- Floating-point number
  - float 32bit
  - float 64bit
- Boolean: true / false

- Pointer

### Data Structure

- Set
- Map
- Array (Vector)
- Matrix
- Structure
- Deque
- Function