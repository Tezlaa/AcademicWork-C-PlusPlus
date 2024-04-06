
class Sets:
    methods_name = 'method'

    def __init__(self, sets: list[set]) -> None:
        self.sets = sets

    def create_report(self) -> dict[str, bool]:
        report = {}
        for method_name in dir(self):
            if not method_name.startswith(f'{self.methods_name}_'):
                continue
            clear_method_name = method_name.replace(f'{self.methods_name}_', '')
            report[clear_method_name] = self.__getattribute__(method_name)()
        return report

    def method_is_matching(self) -> bool:
        return all(_set == self.sets[0] for _set in self.sets[1:])

    def method_is_intersection(self) -> bool:
        for i in range(len(self.sets)):
            for j in range(i + 1, len(self.sets)):
                if self.sets[i] & self.sets[j]:
                    return True
        return False


def input_sets() -> list[set]:
    result = []
    print(
        ('Example: 1, 2, 3. It`s translate to -> {1, 2, 3}\n'),
        ('Send: `save` for save and start')
    )
    while True:
        user_input = input()
        if user_input == 'save':
            return result
        result.append(set(user_input.split(', ')))


def print_sets(reports: dict[str, bool]) -> None:
    max_method_name = len(max(reports.keys(), key=lambda x: len(x)))

    print('_' * 21)
    for name, value in reports.items():
        indent = max_method_name - len(name)
        print(
            f'| {name} {" " * indent if indent > 0 else ""}'
            f'| {"V" if value else "X"}'
        )

    print('-' * 21)


if __name__ == '__main__':
    while True:
        user_set = input_sets()
        result = Sets(user_set).create_report()
        print_sets(result)
