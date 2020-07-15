def cakes(recipe, available):
    amount = []
    for item in recipe.keys():
        if available.get(item):
            amount.append(available.get(item) / recipe.get(item))
        else:
            amount.append(0)
            break
    amount.sort()
    return int(amount[0])

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available) == 2)
print("")
recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available) == 0)

