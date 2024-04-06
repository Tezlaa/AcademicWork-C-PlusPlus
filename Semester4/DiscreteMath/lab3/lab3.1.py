
class Child:
    def __init__(self, descendants) -> None:
        self.descendants = descendants
        self.roots = []

    def search_child(self, name: str):
        if descendants.get(name):
            return self.search_child_that_boss(name)
        return self.search_child_that_not_boss(name)

    def search_child_that_boss(self, name: str):
        for child in self.descendants.get(name):
            self.search_child(child)

    def search_child_that_not_boss(self, name: str):
        self.roots.append(name)

    def find_youngest_child(self, name: str) -> str:
        self.search_child(name)
        youngest_child = self.roots[-1]
        self.roots.clear()
        return youngest_child


if __name__ == '__main__':
    # users: NAME_1: (NAME_2(high), ..., NAME_3(low))
    descendants = {
        "Alice": ["Bob", "Charlie"],
        "Bob": ["David", "Emily"],
        "Charlie": ["Fiona"]
    }

    child = Child(descendants)
    while True:
        print(f'\nSelected name: \n{',\n'.join([f'boss: {boss} - child: ({', '.join(child)})' for boss, child in descendants.items()])}')
        find_name = input('>>> ')
        print(f'\n\nYoungest child: {child.find_youngest_child(find_name)}')
