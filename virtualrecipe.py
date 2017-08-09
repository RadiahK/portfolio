recipe = {"Shrimp Avocado Salad":["1/4 cup mayonnaise"
"2 stalks celery", "thinly sliced", "plus 3 tablespoons",
"chopped celery leaves",
"3 tablespoons finely chopped fresh cilantro",
"Kosher salt and freshly ground pepper",
"1 1/2 limes","1 1/2 pounds large shrimp peeled and deveined",
"1 tablespoon vegetable oil","2 hass avocados, diced",
"1 5-ounce package baby kale salad mix (about 8 cups)",
"1 small bunch radishes, thinly sliced"], ["Preheat a grill or grill pan to medium high.",

"Make the dressing. Combine the mayonnaise, celery leaves, 2 tablespoons chopped cilantro, 1 tablespoon water, 1/2 teaspoon salt and a few grinds of pepper in a large bowl.", "Grate in the zest of 1 lime and squeeze in the juice.",

"Toss the shrimp with the vegetable oil, 1/4 teaspoon salt and a few grinds of pepper in a bowl.", "Arrange the shrimp on the grill and cook until pink and just firm, about 2 minutes per side.", "Transfer to the bowl with the dressing; squeeze in the juice of the remaining 1/2 lime.",

"Add the sliced celery, avocados, salad mix and radishes to the bowl with the shrimp; toss to coat.", "Top with the remaining 1 tablespoon chopped cilantro."]]}
print "What recipe would you like?"
recipes = dict.keys()
for x in range(len(recipe)):
    print (recipes[x])
    recipe[x] = recipes.[x]


recipeBox = ""
while recipe not in recipes:
    recipe = input ("Recipe Name: ").title()

print (recipe)
print()
print("Ingredients:")
for y in recipeBox[recipe][0]:
    print (y)
print()
print ("Directions:")
for y in range (len(recipeBox[recipe][1])):
    print(str(y+1) + ". " + recipeBox[recipe][1][y])
