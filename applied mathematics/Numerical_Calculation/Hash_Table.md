# Hash Table

[TOC]

## Define

**Hash table** is a data structure that implements an associative array, also called a dictionary, which is an abstract data type that maps keys to values.
$$
\{(key, value)\}
$$
A hash function maps $h: U\to \{0, \cdots, m-1\}$ the universe $U$ of keys to indices or slots within the table.

## Property

**Load factor**, where $n$ is the number of entries occupied in the hash table. $m$ is the number of buckets.
$$
\text{Load factor}(\alpha) = \frac{n}{m}
$$

### Collision resolution

**Separate chaining**

**Open addressing**
