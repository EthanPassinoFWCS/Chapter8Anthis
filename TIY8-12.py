def sandwich(*ingredients):
    print("The sandwich has ")
    for ingredient in ingredients:
        print(f"{ingredient}")


sandwich("Ham", "Cheese")
print("")
sandwich("Turkey")
print("")
sandwich("Ham", "Turkey", "Cheese")
