from itertools import product


def count_outfits(types, colors, rules):
    outfits = 0
    for type_combo in product(types, repeat=len(colors)):
        if all(rule(type_combo) for rule in rules):
            outfits += 1
    return outfits


def main(types: list[str], colors: list[str]):
    rules = [
        lambda combo: "blue" not in combo or "cyan" not in combo,
        lambda combo: "green" not in combo or "pink" not in combo,
        lambda combo: "green" not in combo or "red" not in combo,
        lambda combo: combo[0] != "bag" or combo[1] != "dress"
    ]

    total_outfits = count_outfits(types, colors, rules)
    print("Barbie can create", total_outfits, "different outfits.\n\n")


if __name__ == "__main__":
    main(["dress", "shoes", "bag", "hat"], ["white", "pink", "red", "blue", "cyan", "yellow", "green", "black"])
    main(["shirt", "pants", "shoes", "belt"], ["white", "black", "gray"])
    main(["top", "skirt", "sandals", "necklace"], ["blue", "yellow", "green", "silver"])
