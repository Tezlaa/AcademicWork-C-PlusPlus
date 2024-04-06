ice_cream_flavors = {'Vanilla', 'Chocolate', 'Strawberry', 'Caramel', 'Mint', 'Hazelnut', 'Coffee'}
toppings = {'Chocolate sauce', 'Caramel sauce', 'Marshmallow', 'Nuts', 'Wafers', 'Fruits'}

if __name__ == '__main__':
    menu = []

    for flavor in ice_cream_flavors:
        for topping in toppings:
            menu.append(f"{flavor} with {topping}")

    # Print the menu
    for item in menu:
        print(item)
