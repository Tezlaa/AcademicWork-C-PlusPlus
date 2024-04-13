from collections import defaultdict

def simplify_debts(debts):
    debtors = defaultdict(int)
    creditors = defaultdict(int)

    for debtor, creditor, amount in debts:
        debtors[debtor] += amount
        creditors[creditor] += amount

    simplified_debts = []

    for person in debtors:
        if debtors[person] > 0:
            for counterparty in creditors:
                if creditors[counterparty] > 0:
                    settled_amount = min(debtors[person], creditors[counterparty])
                    if settled_amount > 0:
                        simplified_debts.append((person, counterparty, settled_amount))
                        debtors[person] -= settled_amount
                        creditors[counterparty] -= settled_amount
                        if debtors[person] == 0:
                            break

    return simplified_debts


if __name__ == '__main__':
    debts_1 = [
        ("Alice", "Bob", 100),
        ("Bob", "Alice", 50),
        ("Alice", "Charlie", 30),
        ("Charlie", "Bob", 20)
    ]
    debts_2 = [
        ("Alice", "Bob", 200),
        ("Bob", "Charlie", 100),
        ("Charlie", "Alice", 150),
        ("David", "Alice", 50)
    ]
    debts_3 = [
        ("Alice", "Bob", 300),
        ("Bob", "Charlie", 200),
        ("Charlie", "Alice", 100),
        ("David", "Bob", 150),
        ("Eve", "Alice", 50)
    ]

    for debts in [debts_1, debts_2, debts_3]:
        simplified_debts = simplify_debts(debts)

        for debtor, creditor, amount in simplified_debts:
            print(f"{debtor} must pay {amount} {creditor}")

        print('\n\n')
