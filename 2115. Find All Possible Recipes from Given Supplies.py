class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        available = set(supplies)
        needs = {r: set(ing) for r, ing in zip(recipes, ingredients)}

        updated = True
        while updated:
            updated = False
            for r in recipes:
                if r in available:
                    continue
                
                if needs[r].issubset(available):  # All ingredients available? We cookin'
                    available.add(r)
                    updated = True
        
        return [r for r in recipes if r in available]