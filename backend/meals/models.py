from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.JSONField(default=list, blank=True)
    instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class CookingLog(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    cooked_on = models.DateField()

class MealPlan(models.Model):
    # Container of planned recipes
    week_start = models.DateField(unique=True)

class PlannedRecipe(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)