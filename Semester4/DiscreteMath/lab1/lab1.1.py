def generate_subsets(numbers: set) -> list[set]:
    result = [[]]
    for num in numbers:
        result += [subset + [num] for subset in result]
    return ([set(subset) for subset in result])


def print_subsets(numbers: set):
    subsets = generate_subsets(numbers)
    for subset in subsets:
        print(subset if subset else set())
    print('\n\n\n')


if __name__ == "__main__":
    print_subsets(
        {1, 2, 3}
    )
    print_subsets(
        {1, 2, 3, 4, 3, 3, 1, 5, 2}
    )
    print_subsets(
        {324, 2341, 132414}
    )
