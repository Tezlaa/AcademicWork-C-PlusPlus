from typing import Optional


def possible_subsets(word: str) -> list[set]:
    result = [[]]
    for char in word:
        result += [subset + [char] for subset in result]

    return [set(subset) for subset in result]


def combination_subsets(subsets: list[set],
                        excluding: Optional[set] = None) -> set[str]:
    excluding = set() if not excluding else excluding
    result = []
    for subset in subsets:
        str_subset = ''.join(subset)
        if str_subset not in excluding:
            result.append(str_subset)
    return set(result)


if __name__ == '__main__':
    test_sets = (
        {'ab', 'cb'},
        {'ab', 'gd', 'df'},
        {'qd', 'b'},
        {'a'},
    )
    for test_number, test_set in enumerate(test_sets, start=1):
        joined_subset = ''.join(test_set)
        subsets = possible_subsets(joined_subset)
        result = combination_subsets(subsets, excluding=test_set)

        print(f'\nTest №{test_number}\n{"_" * 10}')
        for chars in result:
            print(f'| {chars} |')
