from collections import defaultdict

def find_boss(records):
    subordinates = defaultdict(list)
    count = defaultdict(int)

    for record in records:
        boss, subordinate = record.split(' performed task for ')
        subordinates[boss].append(subordinate)
        count[subordinate] += 1

    potential_boss = None
    for person in subordinates.keys():
        if count[person] == 0:
            if potential_boss is not None:
                return None
            potential_boss = person

    return potential_boss


if __name__ == '__main__':
    # Variations of input data
    records_var1 = [
        "John performed task for Mike",
        "Mike performed task for Bob",
        "Bob performed task for Alice"
    ]

    records_var2 = [
        "Alice performed task for Bob",
        "Bob performed task for John",
        "John performed task for Mike",
        "Mike performed task for Alice"
    ]

    records_var3 = [
        "Bob performed task for Alice",
        "Alice performed task for Mike",
        "Mike performed task for John"
    ]

    for record in [records_var1, records_var2, records_var3]:
        boss = find_boss(record)
        if boss:
            print(f"Mafia boss: {boss}")
        else:
            print("Failed to determine the mafia boss")
