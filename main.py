from utils import converter
from store.menus import show_menu

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    weight = float(input("Enter your weight: "))
    is_kg = ""
    while is_kg.lower() not in ["y", "n"]:
        is_kg = input("Is that in Kilograms (Y|N) ? ").lower()
        if is_kg not in ["y", "n"]:
            print('Unrecognized Command ! Please enter "Y" or "N"')


    if is_kg == "y":
        weight = converter.kg_to_lbs(weight)
    else:
        weight = converter.lbs_to_kg(weight)


    foods = show_menu()
    i = 0
    print("Our Menu today:")
    for food in foods:
        print(f"{i} - {food.get('name')} ($ {food.get('price')})")
        i += 1


    opt = 0
    while True:
        try:
            opt = int(input(f"Enter your choice [0-{len(foods)-1}]: "))
        except ValueError:
            print(f"Invalid Entry. Please entry a number between 0 and {len(foods)-1}!")
        else:
            break

    total_tax = foods[opt].get('price') * 10.0
    total_cost = foods[opt].get('price') + total_tax
    print(f"You have choosen {foods[opt].get('name')}")
    print(f"Sub Total: $ {foods[opt].get('price')}")
    print(f"Tax: $ {total_tax}")
    print(f'Please pay ${total_cost} to cashier. Thank You.')


if __name__ == '__main__':
    main()
