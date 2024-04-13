from lab6_1 import CalculateBit


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
        formula_1 = input('formula 1 >>>')
        formula_2 = input('formula 2 >>>')
        result_1 = bitcalculation.result(formula_1)
        result_2 = bitcalculation.result(formula_2)

        print('formulas equivalent: ', int(result_1 == result_2))
