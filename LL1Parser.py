class LL1Parser:
    def __init__(self, grammar):
        """
        Initialize the LL(1) parser with a given grammar.
        :param grammar: A dictionary representing the grammar rules.
        """
        self.grammar = grammar
        self.non_terminals = set(grammar.keys())
        self.terminals = set(
            c for productions in grammar.values()
            for production in productions
            for c in production if c not in self.non_terminals and c != 'ε'
        )
        self.terminals.add('ε')  # Include epsilon as a special terminal
        self.first = {symbol: {symbol} for symbol in self.terminals}
        self.first.update({non_terminal: set() for non_terminal in self.non_terminals})
        self.follow = {non_terminal: set() for non_terminal in self.non_terminals}
        self.parsing_table = {}
        self.start_symbol = list(grammar.keys())[0]  # Assume the first grammar rule is the start symbol

    def compute_first(self):
        """
        Compute the First sets for all non-terminals in the grammar.
        """
        def first_of(symbol):
            """
            Recursive function to calculate the First set of a symbol.
            :param symbol: The grammar symbol (terminal or non-terminal).
            :return: The First set of the symbol.
            """
            if symbol in self.terminals:
                return {symbol}
            if self.first[symbol]:  # Already computed
                return self.first[symbol]
            for production in self.grammar.get(symbol, []):
                for char in production:
                    if char == 'ε':  # Handle epsilon directly
                        self.first[symbol].add('ε')
                        break
                    char_first = first_of(char)
                    self.first[symbol].update(char_first - {'ε'})
                    if 'ε' not in char_first:
                        break
                else:
                    self.first[symbol].add('ε')
            return self.first[symbol]

        for non_terminal in self.non_terminals:
            first_of(non_terminal)

    def compute_follow(self):
        """
        Compute the Follow sets for all non-terminals in the grammar.
        """
        self.follow[self.start_symbol].add('$')  # Add end-of-input symbol to the start symbol's Follow set

        def follow_of(non_terminal):
            """
            Function to calculate the Follow set of a non-terminal.
            :param non_terminal: The non-terminal to calculate the Follow set for.
            """
            for head, productions in self.grammar.items():
                for production in productions:
                    for i, symbol in enumerate(production):
                        if symbol == non_terminal:
                            next_symbols = production[i + 1:]
                            if next_symbols:
                                for next_symbol in next_symbols:
                                    self.follow[non_terminal].update(self.first[next_symbol] - {'ε'})
                                    if 'ε' not in self.first[next_symbol]:
                                        break
                                else:
                                    self.follow[non_terminal].update(self.follow[head])
                            else:
                                self.follow[non_terminal].update(self.follow[head])

        for _ in self.grammar:
            for non_terminal in self.non_terminals:
                follow_of(non_terminal)

    def build_parsing_table(self):
        """
        Build the LL(1) parsing table based on the grammar's First and Follow sets.
        """
        for non_terminal in self.grammar:
            for production in self.grammar[non_terminal]:
                for terminal in self.first_of_production(production):
                    if terminal != 'ε':
                        self.parsing_table[(non_terminal, terminal)] = production
                if 'ε' in self.first_of_production(production):
                    for terminal in self.follow[non_terminal]:
                        self.parsing_table[(non_terminal, terminal)] = production

    def first_of_production(self, production):
        """
        Calculate the First set of a production.
        :param production: A list of grammar symbols in the production.
        :return: The First set of the production.
        """
        result = set()
        for symbol in production:
            symbol_first = self.first.get(symbol, {symbol})
            result.update(symbol_first - {'ε'})
            if 'ε' not in symbol_first:
                break
        else:
            result.add('ε')
        return result

    def is_ambiguous(self):
        """
        Check if the grammar is ambiguous by identifying multiple entries in any cell of the parsing table.
        :return: True if ambiguous, False otherwise.
        """
        cells = {}
        for (non_terminal, terminal), production in self.parsing_table.items():
            if (non_terminal, terminal) in cells:
                return True
            cells[(non_terminal, terminal)] = production
        return False

    def print_parsing_table(self):
        """
        Print the LL(1) parsing table in a readable format.
        """
        print("Parsing Table:")
        for (non_terminal, terminal), production in sorted(self.parsing_table.items()):
            print(f"M[{non_terminal}, {terminal}] = {production}")


if __name__ == "__main__":
    # Define a sample grammar
    grammar = {
        'E': ['TX'],
        'X': ['+TX', 'ε'],  # 'ε' represents epsilon (empty string)
        'T': ['FY'],
        'Y': ['*FY', 'ε'],
        'F': ['(E)', 'id']
    }

    # Initialize the LL(1) parser
    parser = LL1Parser(grammar)

    # Compute First and Follow sets
    parser.compute_first()
    parser.compute_follow()

    # Build the parsing table
    parser.build_parsing_table()

    # Print First sets
    print("First sets:")
    for non_terminal, first_set in parser.first.items():
        print(f"First({non_terminal}) = {first_set}")

    # Print Follow sets
    print("\nFollow sets:")
    for non_terminal, follow_set in parser.follow.items():
        print(f"Follow({non_terminal}) = {follow_set}")

    # Print Parsing Table
    print("\nParsing Table:")
    parser.print_parsing_table()

    # Check for ambiguity
    if parser.is_ambiguous():
        print("The grammar is ambiguous or inherently not LL(1).")
    else:
        print("The grammar is valid for LL(1) parsing.")
