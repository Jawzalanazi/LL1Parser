# LL(1) Parser Implementation 🧑‍💻

## Description 📜

This project implements an LL(1) parser in Python that computes the **First** and **Follow** sets for a given grammar and generates an **LL(1) parsing table**. The parser can also check for **ambiguity** in the grammar by ensuring there are no multiple definitions in any cell of the parsing table. 🚀

## Features 🌟

- **Grammar Representation**: Input grammar is provided as a dictionary, where non-terminals are mapped to lists of production rules. 📚
- **First and Follow Sets**: Computes and displays the First and Follow sets for all non-terminals in the grammar. 🔢
- **LL(1) Parsing Table**: Constructs and displays the LL(1) parsing table based on the computed sets. 🗂️
- **Ambiguity Check**: Identifies if the grammar is ambiguous or not LL(1) by checking for multiple definitions in any parsing table cell. ⚠️
- **Test Cases**: Includes test examples to verify the functionality. ✅

## Key Concepts 💡

- **First Sets**: Determines the set of terminals that can appear first in the derivation of a non-terminal. 🔑
- **Follow Sets**: Determines the set of terminals that can follow a non-terminal in a derivation. 📍
- **LL(1) Parsing Table**: Used for predictive parsing to guide the parser's decision-making process. 📊
- **Ambiguity Detection**: Ensures that the grammar is not ambiguous by checking the parsing table for duplicate entries. ❌

## Installation 🔧

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/LL1-Parser.git
```

## Usage 🛠️

1. **Define the Grammar**: Provide a grammar in the form of a dictionary, where keys are non-terminals, and values are lists of production rules.
   
   Example Grammar:

   ```python
   grammar = {
       'E': ['TX'],
       'X': ['+TX', 'ε'],
       'T': ['FY'],
       'Y': ['*FY', 'ε'],
       'F': ['(E)', 'id']
   }
   ```

2. **Initialize the Parser**:

   ```python
   parser = LL1Parser(grammar)
   ```

3. **Compute First and Follow Sets**:

   ```python
   parser.compute_first()
   parser.compute_follow()
   ```

4. **Build and Print the Parsing Table**:

   ```python
   parser.build_parsing_table()
   parser.print_parsing_table()
   ```

5. **Check for Ambiguity**:

   ```python
   if parser.is_ambiguous():
       print("The grammar is ambiguous or inherently not LL(1).")
   else:
       print("The grammar is valid for LL(1) parsing.")
   ```

## Example Output 📊

### First Sets:
```
First(E) = {'(', 'id'}
First(X) = {'+', 'ε'}
First(T) = {'(', 'id'}
First(Y) = {'*', 'ε'}
First(F) = {'(', 'id'}
```

### Follow Sets:
```
Follow(E) = {')', '$'}
Follow(X) = {')', '$'}
Follow(T) = {'+', ')', '$'}
Follow(Y) = {'+', ')', '$'}
Follow(F) = {'*', '+', ')', '$'}
```

### Parsing Table:
```
Parsing Table:
M[E, (] = TX
M[X, +] = +TX
M[T, (] = FY
M[Y, *] = *FY
M[F, (] = (E)
M[F, id] = id
```

### Ambiguity Check:
```
The grammar is valid for LL(1) parsing. 🎉
```

## Demo 🎥

- **Objective:** Demonstrate the functionality of the LL(1) parser and the parsing table generation.
- **Test Cases:** Includes at least two test examples to verify correctness. 🔍

## License 📝

This project is provided for educational purposes.
Feel free to use or adapt it with credit.
