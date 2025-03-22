# Hash Table

[TOC]

## Define

$$
\{(key, value)\}
$$

**Hash table** is a special collection used to store $keys \to values$ pairs that provide key retrieval capabilities $find: \{key\} \to \{value\}$. Specifically, hash table uses a hash function $f: \{key\} \to \mathbb N$ to map keys to indices in an array within the range of the hash table's size.

## Property

### Operations



### Load factor

$$
\text{Load factor}(\alpha) = \frac{n}{m}
$$

Load factor reflects the ratio of the number of key-values stored in the hash table to its total capacity. As the load factor increases, the probability of hash table collisions also increases.

- $n$: the number of entries occupied in the hash table.
- $m$: the number of buckets.


### Hash table collision

A hash function takes a key as input and returns an index within the range of the hash table's size. However, it is possible for two different keys to be mapped to the same index by the hash function. This situation is called a hash table collision.

#### Separate chaining

When a hash function maps multiple keys to the same index in the hash table, instead of storing only one key-value pair at that index, a linked list (or other data structure like a binary search tree) is maintained at each index of the hash table. Each element that hashes to a particular index is inserted into the linked list at that index.

#### Open addressing

when a collision occurs, the algorithm searches for the next available slot in the hash table to store the key-value pair. There are several ways to search for the next available slot, including linear probing, quadratic probing, and double hashing.
