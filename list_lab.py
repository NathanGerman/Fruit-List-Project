def series1():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print(fruits)

    new_fruit = input("Add another fruit: ")
    fruits.append(new_fruit)
    print(fruits)

    number = int(input(f"Pick a number (1-{len(fruits)}): "))
    print(f"You picked {fruits[number - 1]}")

    fruits = ["Mango"] + fruits
    print(fruits)

    fruits.insert(0, "Grapes")
    print(fruits)

    print("Fruits that start with P:")
    for fruit in fruits:
        if fruit[0].lower() == "p":
            print(fruit)

    return fruits


def series2(fruits):
    print(fruits)
    fruits.pop()
    print(fruits)

    fruit = input("Enter a fruit to delete: ")
    if fruit in fruits:
        fruits.remove(fruit)
    print(fruits)

    fruits *= 2
    while True:
        fruit = input("Enter a fruit to delete (list doubled): ")
        if fruit in fruits:
            while fruit in fruits:
                fruits.remove(fruit)
            break
        else:
            print("Notfound. Try again.")
    print(fruits)


def series3(fruits):
    liked = fruits[:]
    for fruit in fruits:
        while True:
            answer = input(f"Do you like {fruit.lower()}? (yes/no): ").lower()
            if answer == "no":
                liked.remove(fruit)
                break
            elif answer == "yes":
                break
            else:
                print("Please type yes or no.")
    print(liked)


def series4(fruits):
    reversed_list = [fruit[::-1] for fruit in fruits]
    fruits.pop()
    print("Original list:", fruits)
    print("Reversed list:", reversed_list)


def main():
    fruits = series1()
    series2(fruits[:])
    series3(fruits[:])
    series4(fruits[:])


if __name__ == "__main__":
    main()
