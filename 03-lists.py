numbers = [1, 2, 3, 4, 5]
fruit = ["Banana", "Oranges", "Grapes", "Strawberry", "Apple"]
fruit.sort()


print(fruit)

fruit[1] = "Updated fruit"

fruit.extend(numbers)
fruit.append("Banana")
fruit.insert(2, "Banana")
fruit.remove(3)

bananaCount = fruit.count("Banana")

print(str(bananaCount) + " x banana's")

print(fruit)

fruit.clear()

print(fruit)