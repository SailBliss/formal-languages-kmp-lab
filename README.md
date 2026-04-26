# kmp-lab-python

Implementation of the KMP string-matching algorithm in Python, based on Section 3.4.5 and Figure 3.20 of *Compilers: Principles, Techniques, & Tools* (Aho et al., 2nd ed.).

## Environment

- Operating system: Windows 11
- Python version: 3.13.7
- Tools: Git, Visual Studio Code

## Project structure

```
kmp-lab-python/
├── failure.py      # failure function (prefix-suffix table)
├── kmp.py          # KMP search algorithm
├── examples.py     # usage examples
├── docs/
│   └── hw-2.pdf    # assignment reference
└── README.md
```

## How to run

```bash
python examples.py
```

To test individual functions:

```bash
python -c "from failure import compute_failure; print(compute_failure('ababaa'))"
# [0, 0, 1, 2, 3, 1]

python -c "from kmp import kmp_search; print(kmp_search('abababaab', 'ababaa'))"
# [2]
```

## Algorithms

### Failure function -> `failure.py`

Computes the failure table for a given pattern. Each position `i` stores the length of the longest proper prefix of `pattern[0..i]` that is also a suffix of that same segment.

This table is the core of KMP: it tells the algorithm how far to fall back in the pattern after a mismatch, without moving backward in the text.

Example for pattern `ababaa`:

```
pattern : a  b  a  b  a  a
failure : 0  0  1  2  3  1
```

### KMP search -> `kmp.py`

Searches for all occurrences of a pattern in a text in O(n + m) time, where n is the length of the text and m is the length of the pattern. The text index never moves backward.

## Exercise 3.4.6

Apply the KMP algorithm to test whether `ababaa` is a substring of:

**Failure table for `ababaa`:** `[0, 0, 1, 2, 3, 1]`

### a) `abababaab`

| i | j | text[i] | pattern[j] | match? | action |
|---|---|---------|------------|--------|--------|
| 0 | 0 | a | a | yes | i=1, j=1 |
| 1 | 1 | b | b | yes | i=2, j=2 |
| 2 | 2 | a | a | yes | i=3, j=3 |
| 3 | 3 | b | b | yes | i=4, j=4 |
| 4 | 4 | a | a | yes | i=5, j=5 |
| 5 | 5 | b | a | no | j = failure[4] = 3 |
| 5 | 3 | b | b | yes | i=6, j=4 |
| 6 | 4 | a | a | yes | i=7, j=5 |
| 7 | 5 | a | a | yes | i=8, j=6 -> **match at position 2** |

**Result: `ababaa` is found at position 2.** 

### b) `abababbaa`

| i | j | text[i] | pattern[j] | match? | action |
|---|---|---------|------------|--------|--------|
| 0 | 0 | a | a | yes | i=1, j=1 |
| 1 | 1 | b | b | yes | i=2, j=2 |
| 2 | 2 | a | a | yes | i=3, j=3 |
| 3 | 3 | b | b | yes | i=4, j=4 |
| 4 | 4 | a | a | yes | i=5, j=5 |
| 5 | 5 | b | a | no | j = failure[4] = 3 |
| 5 | 3 | b | b | yes | i=6, j=4 |
| 6 | 4 | b | a | no | j = failure[3] = 2 |
| 6 | 2 | b | a | no | j = failure[1] = 0 |
| 6 | 0 | b | a | no | i=7, j=0 |
| 7 | 0 | a | a | yes | i=8, j=1 |
| 8 | 1 | a | b | no | j = failure[0] = 0, i=9 |

**Result: `ababaa` is not found.** 

## AI usage declaration

This project was developed with the assistance of Claude (Anthropic) as a learning tool.

Claude was used to:
- Explain the concepts of the failure function and the KMP algorithm step by step.
- Help understand the pseudocode before writing the code.
- Format this README file for aesthetic reasons.

The whole code was written by hand. AI was used only as a tutor to understand concepts and did not replaced the process.
