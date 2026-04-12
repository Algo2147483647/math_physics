# Logic

[TOC]

## Define

### Proposition

A proposition is a declarative sentence that can be judged true or false, but cannot be both true and false.

#### Axioms

An axiom is a statement that is taken to be true, to serve as a premise or starting point for further reasoning and arguments. 

#### Theorems

Theorems are propositions obtained using axioms and inference rules. Once a proposition is proven as a theorem, it can also be used as a basis for further reasoning.

### Logical syntax
#### Logical connective

Logical connective can be used to connect logical formulas. 

- Negation (not) $\neg$
- Conjunction (and) $\wedge$
- Disjunction (or) $\vee$
- Implication (if...then) $\rightarrow$
- Equivalence (if and only if, iff) $\leftrightarrow$

<img src="assets/Logical_connectives_Hasse_diagram.svg" alt="Logical_connectives_Hasse_diagram" style="zoom: 33%;" />

#### Constants

- true $\top$
- false $\bot$

#### Relative words

- equal to $=$
- belong to $\in$

#### Predicate

Predicates are symbols or expressions used to describe object attributes or relationships between objects.

- **Predicate** $P (x), Q (x), R (x), \cdots$: usually representing an object with a certain property, where $x$ is a variable

- **Constants** $a, b, c, \cdots$: representing specific individuals or objects

- Variable $x, y, z, \cdots$: used to represent any individual or object

#### Quantifier

Quantifier specify the quantity of specimens in the domain of discourse that satisfy a certain property. 

- **Universal quantifier** (for all) $\forall$
- **Existential quantifier** (there exists) $\exists$ 
  - **Uniqueness quantifier** (there is only one) $\exists_{=1}$


### Axiomatic system

Axiom system is composed of a set of axioms (basic, unproven true statements) and a set of inference rules. It provides a framework that enables us to derive new true statements (theorems) from axioms and inference rules.

## Properties

- Consistency: A system of axioms is consistent, and both if and only if there is no proposition and its negation can be proven from the axioms of that system.

- Completeness: A system of axioms is complete if and only if every true proposition of the system can be proven from its axioms.


### Gödel's incompleteness theorems

- First Incompleteness Theorem: Any consistent formal system F within which a certain amount of elementary arithmetic can be carried out is incomplete; i.e., there are statements of the language of F which can neither be proved nor disproved in F.
- Second Incompleteness Theorem: For any consistent system F within which a certain amount of elementary arithmetic can be carried out, the consistency of F cannot be proved in F itself.

## Include

## Parents

