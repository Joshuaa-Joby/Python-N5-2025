
ingredients = {
    "flour (g)": 200,
    "butter (g)": 100,
    "sugar (g)": 80,
    "eggs": 2,
    "chocolate chips (g)": 150,
    "vanilla (tsp)": 1
}


original_servings = 4
new_servings = 6

scaling_factor = new_servings / original_servings
scaled_ingredients = {}
for item, amount in ingredients.items():
    scaled_ingredients[item] = round(amount * scaling_factor, 2) if isinstance(amount, (int, float)) else amount

print(f"Ingredients for {new_servings} people:")