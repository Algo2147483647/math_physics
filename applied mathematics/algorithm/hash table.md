# Hash Table

[TOC]

## Problem

A hash table is designed to solve the problem of **fast data lookup by key**.

- Does this key already exist?
- What value is associated with this key?
- How can I insert or delete a key efficiently?

## Core Idea

A hash table addresses this by providing an efficient structure for:

- **insertion**
- **search**
- **deletion**

under average conditions, typically in **O(1)** time.

The core idea of a hash table is to use a **hash function** to map a key to an array index. Instead of searching through all elements, we compute:
$$
index = hash(key)
$$
and place the key-value pair directly into the corresponding bucket or slot. This turns the problem of lookup from “search the whole dataset” into “jump directly to the likely location.” However, different keys may produce the same index. This is called a **collision**. Therefore, the practical essence of a hash table is:

1. **Use hashing to narrow lookup to a small location**
2. **Use a collision-handling strategy to manage overlaps efficiently**

So the performance of a hash table depends on:

- the quality of the hash function
- the collision resolution method
- the load factor of the table



$$
\{(key, value)\}
$$

**Hash table** is a special collection used to store $keys \to values$ pairs that provide key retrieval capabilities $find: \{key\} \to \{value\}$. Specifically, hash table uses a hash function $f: \{key\} \to \mathbb N$ to map keys to indices in an array within the range of the hash table's size.

## Solution

### Underlying Storage

Usually, a hash table is backed by an **array** of fixed or dynamically resized buckets. Each bucket can store:

- a single entry, or
- multiple entries if collisions occur

### Hash Function

A hash function takes a key as input and returns an index within the range of the hash table's size. However, it is possible for two different keys to be mapped to the same index by the hash function. This situation is called a hash table collision.

The hash function converts a key into an integer hash code, which is then mapped into the table range. Example: $index = hash(key) % capacity$. A good hash function should:

* be deterministic
* distribute keys evenly
* minimize collisions
* be fast to compute

### Collision Resolution

Since collisions are unavoidable, the implementation must define how to handle them.

#### Separate Chaining

When a hash function maps multiple keys to the same index in the hash table, instead of storing only one key-value pair at that index, a linked list (or other data structure like a binary search tree) is maintained at each index of the hash table. Each element that hashes to a particular index is inserted into the linked list at that index.

Each bucket stores a list or chain of entries. This is simple and flexible.

* Insert: append to the chain
* Search: scan the chain for the key
* Delete: remove the matching node

#### Open Addressing

when a collision occurs, the algorithm searches for the next available slot in the hash table to store the key-value pair. There are several ways to search for the next available slot, including linear probing, quadratic probing, and double hashing.

When a collision occurs, probe other slots until an empty or matching slot is found. Common probing methods as follower. This avoids extra linked structures but is more sensitive to clustering and load factor.

* linear probing
* quadratic probing
* double hashing

### Dynamic Resizing

#### Load factor

$$
\text{Load factor}(\alpha) = \frac{n}{m}
$$

Load factor reflects the ratio of the number of key-values stored in the hash table to its total capacity. As the load factor increases, the probability of hash table collisions also increases.

- $n$: the number of entries occupied in the hash table.
- $m$: the number of buckets.

As more elements are inserted, collisions become more frequent. To maintain performance, the table is usually resized when the **load factor** exceeds a threshold.

$$
load factor = number of elements / table capacity
$$
When resizing:

* allocate a larger array
* recompute positions for all existing keys
* reinsert them into the new table

This process is called **rehashing**.

### Core Operations

#### Insert

* Compute the bucket index from the key
* Handle collisions if necessary
* Store the key-value pair

#### Search

* Compute the bucket index
* Look in the bucket or probing sequence
* Return the value if found

#### Delete

* Locate the key
* Remove it while preserving the collision structure

Under normal conditions, these operations are **O(1) on average**.

##  Boundaries

### No Ordering Guarantee

Hash tables do not naturally preserve:

* insertion order
* sorted order
* range order

So they are not suitable when you need operations like:

* finding the minimum or maximum key
* iterating in sorted order
* range queries

For such cases, structures like **balanced trees** are more appropriate.

### Performance Depends on Hash Quality

If the hash function is poor, many keys may map to the same bucket, causing heavy collisions.
In the worst case, operations degrade from **O(1)** to **O(n)**.

### Space Overhead

A hash table often uses extra memory because:

* the underlying array may contain many empty slots
* chaining may require additional node objects or pointers
* resizing temporarily increases memory usage

### Expensive Rehashing

Although infrequent, resizing can be costly because all existing entries must be reinserted.
This makes performance occasionally non-uniform.

### Key Requirements

Hash tables work best when keys:

* can be hashed efficiently
* have stable equality semantics
* do not change after insertion

Mutable keys can break correctness if their hash value changes while stored.

## Cost


The main cost of a hash table lies in the trade-off between **time efficiency** and **space / maintenance overhead**.

### Time Cost

* **Average-case**

  * Insert: **O(1)**
  * Search: **O(1)**
  * Delete: **O(1)**

* **Worst-case**

  * Insert: **O(n)**
  * Search: **O(n)**
  * Delete: **O(n)**

Worst-case behavior usually occurs under severe collisions or poor hashing.

### Space Cost

A hash table typically requires **O(n)** space, but the constant factor can be relatively high due to:

* unused capacity
* collision structures
* resizing overhead

### Engineering Cost

In real systems, implementing a robust hash table also requires careful decisions about:

* hash function design
* collision handling strategy
* resizing policy
* load factor threshold
* memory-performance trade-offs

So while the interface looks simple, building a high-quality hash table involves non-trivial engineering choices.
