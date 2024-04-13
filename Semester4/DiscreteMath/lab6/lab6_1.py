class CalculateBit:
    logic_constants = {
        '*': 'and',
        '+': 'or',
        '-': 'not',
    }

    def __init__(self, constants: dict[str, int]) -> None:
        self.constants = constants

    def result(self, formula: str) -> int:
        self.clear_formula = []
        clear_user_formnula = formula.replace(' ', '')
        for symbol in clear_user_formnula:
            if symbol in self.constants:
                self.clear_formula.append(
                    self.value_from_constants(symbol)
                )
            elif symbol in self.logic_constants:
                self.clear_formula.append(
                    self.value_from_logic_constants(symbol)
                )
            else:
                self.clear_formula.append(symbol)

        result_formula = ' '.join(self.clear_formula)
        print(f'Formula: {result_formula}')
        return int(eval(result_formula))

    def value_from_constants(self, symbol: str) -> str:
        return str(self.constants.get(symbol, ''))

    def value_from_logic_constants(self, symbol: str) -> str:
        return self.logic_constants.get(symbol, '')


if __name__ == '__main__':
    constants = {
        'A': 0,
        'W': 0,
        'B': 1,
        'C': 1,
    }

    print(constants)
    bitcalculation = CalculateBit(constants)
    while True:
        formula = input('>>>')
        print(bitcalculation.result(formula), end='\n\n')
