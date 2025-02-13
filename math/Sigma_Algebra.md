# Sigma Algebra

[TOC]

## Define

$$
  \Sigma \subseteq P(S)  \tag{$\sigma$-algebra}
$$
For a set $S$ and its power set $P(S)$, a $\sigma$-algebra $\Sigma$ is a subset of power set such that
- $S \in \Sigma$, and $S$ is considered to be the universal set in the following context.
- $\Sigma$ closed under complementation, i.e. $A \in \Sigma$ implies that $A^C = S - A \in \Sigma$. Meanwhile, base on the $S \in \Sigma$ (1) we have $\emptyset \in \Sigma$. 
- $\Sigma$ is closed under countable unions, i.e. for any sequence $(A_1, ..., A_n), A_i \in \Sigma$, we have that 
$$
\bigcup_i A_i \in \Sigma
$$

## Properties

- The maximum $\sigma$-algebra is Power Set of $S$,  
The minimum $\sigma$-algebra is $\{\emptyset, S\}$

- Countable intersection set closure, if $A_1, ... , A_n \in Σ$, then $\bigcap_i A_i  \in Σ$
- Proof  
  De Morgan's law

- Include: Borel $\sigma$-algebra

$$
\mathcal B(X) = \sigma(\mathcal O)  \tag{Borel $\sigma$-algebra}
$$
The Borel $\sigma$-algebra on a topological space $X$ is the smallest $\sigma$-algebra containing all the open subsets of $X$. Where $\mathcal O$ denote the collection of all open subsets of $X$.

## Include

## Parents

- [Power_Set](./Power_Set.md): 

