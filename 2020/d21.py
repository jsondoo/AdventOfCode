from collections import defaultdict
import re

f = open('./d21.txt', 'r')
rows = f.read().split("\n")
allergen_to_ingredient = defaultdict(set)

for food in rows:
  parts = food.split("(")
  ingredients = set([x.strip() for x in parts[0].strip().split(" ")])
  allergens = [x.strip() for x in parts[1].replace("contains ", "").replace(")","").split(",")]

  for allergen in allergens:
    if allergen_to_ingredient[allergen]:
      allergen_to_ingredient[allergen] = ingredients.intersection(allergen_to_ingredient[allergen])
    else:
      allergen_to_ingredient[allergen] = ingredients

ingredients_with_allergen = set()
for allergen, ingredients in sorted(allergen_to_ingredient.items(), key= lambda item: len(item[1])):
  ingredients_with_allergen.update(ingredients)

allergen_to_ingredient = {
  "sesame": "kfgln",
  "eggs": "jmvxx",
  "shellfish": "pqqks",
  "fish": "lkv",
  "peanuts": "cbzcgvc",
  "dairy": "fdsfpg",
  "soy": "pqrvc",
  "wheat": "lclnj"
}

print(ingredients_with_allergen)

count = 0
for food in rows:
  parts = food.split("(")
  ingredients = set([x.strip() for x in parts[0].strip().split(" ")])
  for ingredient in ingredients:
    print(ingredient)
    if ingredient not in ingredients_with_allergen:
      count += 1
print(count)

canonical_dangerous_ingredient = ""
for a, i in sorted(allergen_to_ingredient.items(), key= lambda item: item[0]):
  canonical_dangerous_ingredient += i + ","
print(canonical_dangerous_ingredient)